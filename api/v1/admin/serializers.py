from django.db import transaction
from rest_framework import serializers
from rest_framework.fields import ListField, FileField, ImageField

from user.models import Gallery, Menu, PostAttachment, PostImage, Post, GalleryFile


class MenuListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'title', 'parent', 'children', 'is_active')
        extra_kwargs = {
            'children': {'read_only': True},
        }


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'title', 'parent', 'children', 'is_active')
        extra_kwargs = {
            'children': {'read_only': True},
        }

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['children'] = MenuListSerializer(instance.children.all(), many=True).data
        return response

    def update(self, instance, validated_data):
        title = validated_data.pop('title', dict())
        instance.title.update(title)
        return super().update(instance, validated_data)


class PostAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAttachment
        fields = ('id', 'file', 'post')
        read_only_fields = ('id', 'post')


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ('id', 'file', 'post', 'is_active')
        read_only_fields = ('id', 'post')


class PostSerializer(serializers.ModelSerializer):
    attachments = ListField(child=FileField(allow_empty_file=False),
                            required=False,
                            write_only=True,
                            allow_empty=True)
    images = ListField(child=ImageField(allow_empty_file=False),
                       required=False,
                       write_only=True,
                       allow_empty=True)

    menu = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.filter(children=None), required=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            'url',
            'slug',
            'short_content',
            'attachments',
            'images',
            'menu'
        )
        read_only_fields = (
            'id',
        )

    def create(self, validated_data):
        attachments = validated_data.pop('attachments', [])
        images = validated_data.pop('images', [])

        with transaction.atomic():
            post = super().create(validated_data)
            for attachment in attachments:
                PostAttachment.objects.create(post=post,
                                              file=attachment)
            for image in images:
                PostImage.objects.create(post=post,
                                         file=image)

        return post

    def update(self, instance, validated_data):
        title = validated_data.pop('title', dict())
        content = validated_data.pop('content', dict())
        short_content = validated_data.pop('short_content', dict())

        instance.title.update(title)
        instance.content.update(content)
        instance.short_content.update(short_content)

        return super().update(instance, validated_data)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response.update({
            'attachments': PostAttachmentSerializer(instance.attachments.all(),
                                                    context=self.context,
                                                    many=True).data,
            'images': PostImageSerializer(instance.images.all(),
                                          context=self.context,
                                          many=True).data,
        })
        return response


class GalleryFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryFile
        fields = (
            'id',
            'file',
            'gallery',
        )
        read_only_fields = ('id', 'gallery')


class GallerySerializer(serializers.ModelSerializer):
    files = ListField(child=FileField(allow_empty_file=False),
                      required=False,
                      write_only=True,
                      allow_empty=True)

    class Meta:
        model = Gallery
        fields = (
            'id',
            'category',
            'files',
        )
        read_only_fields = ('id', 'files')

    def to_representation(self, instance):
        print(instance)
        data = super(GallerySerializer, self).to_representation(instance)
        data['category'] = instance.get_category_display()
        return data

    def create(self, validated_data):
        print(validated_data)
        files = validated_data.pop('files', [])

        with transaction.atomic():
            gallery, is_created = Gallery.objects.get_or_create(category=validated_data.pop('category'))
            for file in files:
                GalleryFile.objects.create(gallery=gallery, file=file)

        return gallery

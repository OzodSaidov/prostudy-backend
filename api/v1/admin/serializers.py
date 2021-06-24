from django.db import transaction
from rest_framework import serializers
from rest_framework.fields import ListField, FileField, ImageField

from user.models import *


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
        fields = ('id', 'file', 'gallery')
        read_only_fields = ('id', 'gallery')


class GallerySerializer(serializers.ModelSerializer):
    file = serializers.ListField(child=FileField(allow_empty_file=False),
                                 required=False,
                                 write_only=True,
                                 allow_empty=True)
    menu = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.filter(children=None),
                                              required=True,
                                              write_only=True)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), required=True)

    class Meta:
        model = Gallery
        fields = (
            'id',
            'file',
            'course',
            'menu',
        )
        read_only_fields = ('id', 'course', 'menu')

    def create(self, validated_data):
        print(validated_data)
        files = validated_data.pop('file', [])
        with transaction.atomic():
            gallery, is_created = Gallery.objects.get_or_create(validated_data)
            for file in files:
                GalleryFile.objects.create(file=file, gallery=gallery)
        return gallery


class TeacherSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False)

    class Meta:
        model = Teacher
        fields = (
            'id',
            'first_name',
            'last_name',
            'photo',
            'specialty',
            'content_specialty',
            'experience',
        )


class CourseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseImage
        fields = (
            'id',
            'course_image',
            'course',
        )
        read_only_fields = ('id', 'course')


class LessonIconSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseImage
        fields = (
            'id',
            'lesson_icon',
            'course',
        )
        read_only_fields = ('id', 'course')


class CourseSerializer(serializers.ModelSerializer):
    course_image = serializers.ListField(child=ImageField(allow_empty_file=False),
                                         required=False,
                                         write_only=True,
                                         allow_empty=True)
    lesson_icon = serializers.ListField(child=ImageField(allow_empty_file=False),
                                        required=False,
                                        write_only=True,
                                        allow_empty=True)
    menu = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.filter(children=None), required=True)

    class Meta:
        model = Course
        fields = (
            'id',
            'category',
            'title',
            'content',
            'course_image',
            'lesson',
            'lesson_icon',
            'price',
            'menu',
        )
        read_only_field = ('id', 'menu')

    def create(self, validated_data):
        print(validated_data)
        course_images = validated_data.pop('course_image', [])
        lesson_icons = validated_data.pop('lesson_icon', [])
        print(validated_data)
        with transaction.atomic():
            course, is_created = Course.objects.get_or_create(category=validated_data.pop('category'), **validated_data)
            for image in course_images:
                CourseImage.objects.create(course=course, course_image=image)
            for icon in lesson_icons:
                LessonIcon.objects.create(course=course, lesson_icon=icon)

        return course


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = (
            'id',
            'title',
            'content',
            'short_content',
            'image_poster',
            'post',
            'is_active',
        )


class ProgramSerializer(serializers.ModelSerializer):
    image = serializers.ListField(child=FileField(allow_empty_file=False),
                                  required=False,
                                  write_only=True,
                                  allow_empty=True)

    class Meta:
        model = Program
        fields = (
            'id',
            'title',
            'content',
            'image',
        )


class SubscriptionRequest(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionRequest
        fields = '__all__'

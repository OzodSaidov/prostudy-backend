from django.db import transaction
from django.http import Http404
from rest_framework import serializers
from rest_framework.fields import ListField, FileField, ImageField
from rest_framework.generics import get_object_or_404

from user.models import (
    PostImage,
    Feedback,
    Gallery,
    GalleryFile,
    Teacher,
    Advertisement,
    SubscriptionRequest,
    PostAttachment,
    Course,
    Menu,
    Post,
    Program,
    CourseFile,
    LessonIcon,
)


class MenuListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'href', 'title', 'parent', 'children', 'is_active')
        extra_kwargs = {
            'children': {'read_only': True},
        }


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'href', 'title', 'parent', 'children', 'is_active')
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
    file = serializers.ListField(child=FileField(allow_empty_file=False),
                                 required=False,
                                 write_only=True,
                                 allow_empty=True)
    gallery = serializers.PrimaryKeyRelatedField(queryset=Gallery.objects.all())

    class Meta:
        model = GalleryFile
        fields = ('id', 'file', 'gallery')
        read_only_fields = ('id', 'gallery')

    def create(self, validated_data):
        files = validated_data.pop('file', [])
        with transaction.atomic():
            for file in files:
                GalleryFile.objects.create(file=file, **validated_data)
        return super(GalleryFileSerializer, self).data


class GallerySerializer(serializers.ModelSerializer):
    file = serializers.ListField(child=FileField(allow_empty_file=False),
                                 required=False,
                                 write_only=True,
                                 allow_empty=True)
    menu = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.filter(children=None),
                                              required=False)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), required=False)

    class Meta:
        model = Gallery
        fields = (
            'id',
            'title',
            'file',
            'course',
            'menu',
        )
        read_only_fields = ('id', 'course', 'menu')

    def create(self, validated_data):
        files = validated_data.pop('file', [])
        with transaction.atomic():
            try:
                gallery = get_object_or_404(Gallery, course=validated_data.get('course'))
            except Http404:
                gallery = Gallery.objects.create(**validated_data)
            for file in files:
                GalleryFile.objects.create(gallery=gallery, file=file)
        return gallery

    def to_representation(self, instance):
        data = super(GallerySerializer, self).to_representation(instance)
        data['course'] = instance.course.get_category_display()
        data['menu'] = instance.menu.title
        return data

    def update(self, instance, validated_data):
        title = validated_data.pop('title', dict())
        instance.title.update(title)
        return super(GallerySerializer, self).update(instance, validated_data)


class TeacherSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False)
    menu = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.filter(children=None), required=False)

    class Meta:
        model = Teacher
        fields = (
            'id',
            'first_name',
            'last_name',
            'photo',
            'specialty',
            'experience',
            'menu'
        )


class CourseFileSerializer(serializers.ModelSerializer):
    course = serializers.HiddenField(default=None)

    class Meta:
        model = CourseFile
        fields = (
            'id',
            'course_file',
            'course',
        )
        read_only_fields = ('id', 'course')


class LessonIconSerializer(serializers.ModelSerializer):
    course = serializers.HiddenField(default=None)

    class Meta:
        model = LessonIcon
        fields = (
            'id',
            'lesson_icon',
            'course',
        )
        read_only_fields = ('id', 'course')


class CourseSerializer(serializers.ModelSerializer):
    menu = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.filter(children=None), required=False)
    course_file = CourseFileSerializer(source='course_files', many=True)
    lesson_icon = LessonIconSerializer(source='lesson_icons', many=True)

    class Meta:
        model = Course
        fields = (
            'id',
            'category',
            'title',
            'href',
            'content',
            'lesson',
            'price',
            'menu',
            'course_file',
            'lesson_icon',
        )
        read_only_field = ('id', 'menu')

    def update(self, instance, validated_data):
        title = validated_data.pop('title', dict())
        content = validated_data.pop('content', dict())
        lesson = validated_data.pop('lesson', dict())
        price = validated_data.pop('price', dict())

        instance.title.update(title)
        instance.content.update(content)
        instance.lesson.update(lesson)
        instance.price.update(price)

        return super(CourseSerializer, self).update(instance, validated_data)

    def to_representation(self, instance):
        urls = {}
        data = super(CourseSerializer, self).to_representation(instance)
        data['category'] = instance.get_category_display()
        data['menu'] = instance.menu.title
        for file in data['course_file']:
            file_url = file['course_file']
            if file_url.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                urls['image'] = file_url
            elif file_url.endswith(('.mp4', '.mpeg')):
                urls['video'] = file_url
        data['course_file'] = urls
        return data


class AdvertisementSerializer(serializers.ModelSerializer):
    menu = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.filter(children=None), required=False)

    class Meta:
        model = Advertisement
        fields = (
            'id',
            'title',
            'content',
            'short_content',
            'image_poster',
            'is_active',
            'menu'
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
            'course',
        )


class FeedbackSerializer(serializers.ModelSerializer):
    menu = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.filter(children=None), required=False)

    class Meta:
        model = Feedback
        fields = (
            'id',
            'name',
            'email',
            'phone',
            'message',
            'is_active',
            'menu'
        )


class SubscriptionRequestSerializer(serializers.ModelSerializer):
    menu = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.filter(children=None), required=False)

    class Meta:
        model = SubscriptionRequest
        fields = ('id', 'name', 'number_visitors', 'phone', 'is_active', 'menu')

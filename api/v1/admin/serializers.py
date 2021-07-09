from django.db import transaction
from rest_framework import serializers
from rest_framework.fields import ListField, ImageField

from user.models import (
    PostImage,
    Feedback,
    Gallery,
    GalleryFile,
    Teacher,
    Advertisement,
    SubscriptionRequest,
    Course,
    Menu,
    Post,
    Program,
    CourseFile,
    Company, CostOfEducation, Certificate, QuestionAndAnswer, Result, InformationContent,
    InformationContentDetail, AboutUs
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


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ('id', 'file', 'post', 'is_active')
        read_only_fields = ('id', 'post')


class PostSerializer(serializers.ModelSerializer):
    post_images = ListField(child=ImageField(allow_empty_file=False),
                            required=False,
                            write_only=True,
                            allow_empty=True)
    menu = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.filter(children=None), required=False)

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            'url',
            'slug',
            'short_content',
            'post_images',
            'menu',
            'course',
            'program'

        )
        read_only_fields = (
            'id', 'menu'
        )

    def create(self, validated_data):
        images = validated_data.pop('post_images', [])

        with transaction.atomic():
            post = super().create(validated_data)
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

    def to_representation(self, instance: Post):
        data = super(PostSerializer, self).to_representation(instance)
        data.update({
            "post_images": PostImageSerializer(instance.images.all(),
                                               context=self.context, many=True).data
        })
        return data


class GalleryFileSerializer(serializers.ModelSerializer):
    gallery = serializers.HiddenField(default=None)

    class Meta:
        model = GalleryFile
        fields = ('id', 'title', 'src', 'thumbnail', 'url', 'gallery')
        read_only_fields = ('id', 'gallery')


class GallerySerializer(serializers.ModelSerializer):
    menu = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.filter(children=None), required=False)
    file = GalleryFileSerializer(source='gallery_files', many=True)

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
            'about',
            'menu',
            'course'
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


class InformationContentDetailSerializer(serializers.ModelSerializer):
    information_content = serializers.HiddenField(default=None)

    class Meta:
        model = InformationContentDetail
        fields = ('id', 'title', 'body', 'image', 'information_content')


class InformationContentSerializer(serializers.ModelSerializer):
    information_content_detail = InformationContentDetailSerializer(source='content_details', many=True)
    background = serializers.ImageField(required=False)
    course = serializers.HiddenField(default=None)
    program = serializers.HiddenField(default=None)
    menu = serializers.HiddenField(default=None)

    class Meta:
        model = InformationContent
        fields = ('id', 'title', 'body', 'background', 'course', 'program', 'menu',
                  'information_content_detail')


class CostOfEducationSerializer(serializers.ModelSerializer):
    course = serializers.HiddenField(default=None)

    class Meta:
        model = CostOfEducation
        fields = ('id', 'title', 'body', 'old_price', 'new_price', 'image', 'course')


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = (
            'id',
            'title',
            'image',
            'course',
        )


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('id', 'title', 'image', 'course')


class QuestionAndAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAndAnswer
        fields = ('id', 'title', 'description', 'full_description', 'course', 'program')


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('id', 'title', 'content')


class CourseSerializer(serializers.ModelSerializer):
    menu = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.filter(children=None), required=False)
    course_file = CourseFileSerializer(source='course_files', many=True, required=False)

    class Meta:
        model = Course
        fields = (
            'id',
            'category',
            'title',
            'href',
            'menu',
            'course_file',
            'background',
        )
        read_only_field = ('id', 'menu')

    def update(self, instance, validated_data):
        title = validated_data.pop('title', dict())
        instance.title.update(title)
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


class CompanySerializer(serializers.ModelSerializer):
    menu = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.filter(children=None), required=False)

    class Meta:
        model = Company
        fields = ('id', 'title', 'url', 'logo', 'menu')


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ('id', 'image', 'content')


class CourseInformationSerializer(serializers.ModelSerializer):
    course_file = CourseFileSerializer(source='course_files', many=True, required=False)
    teacher = TeacherSerializer(source='teachers', many=True)
    program_training = QuestionAndAnswersSerializer(source='programs_training', many=True)
    result = ResultSerializer(source='results', many=True)
    certificate = CertificateSerializer(source='cert')
    inf_content = InformationContentSerializer(source='inf_contents')
    cost_education = CostOfEducationSerializer(source='cost_educations', many=True)
    program = ProgramSerializer(source='programs', many=True)

    class Meta:
        model = Course
        fields = (
            'id',
            'category',
            'title',
            'href',
            'menu',
            'background',
            'course_file',
            'teacher',
            'program_training',
            'result',
            'certificate',
            'inf_content',
            'cost_education',
            'program'
        )

    def update(self, instance, validated_data):
        title = validated_data.pop('title', dict())
        instance.title.update(title)
        return super(CourseInformationSerializer, self).update(instance, validated_data)

    def to_representation(self, instance):
        urls = {}
        data = super(CourseInformationSerializer, self).to_representation(instance)
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


class ProgramInformationSerializer(serializers.ModelSerializer):
    information_content = InformationContentSerializer(source='inf_contents')
    question = QuestionAndAnswersSerializer(source='questions', many=True)
    post = PostSerializer(source='posts', many=True)

    class Meta:
        model = Program
        fields = (
            'id',
            'title',
            'image',
            'course',
            'information_content',
            'question',
            'post',
        )

    def to_representation(self, instance: Program):
        data = super(ProgramInformationSerializer, self).to_representation(instance)
        qs = instance.course.galleries.gallery_files.all()
        domain = self.context['request'].scheme + '://' + self.context['request'].get_host()
        files = []
        for image in qs:
            context = {
                "src": domain + image.src.url,
                "thumbnail": domain + image.thumbnail.url if image.thumbnail else None
            }
            files.append(context)
        data['gallery'] = files
        return data


class MenuBlogSerializer(serializers.ModelSerializer):
    post = PostSerializer(source='posts', many=True)
    information_content = InformationContentSerializer(source='inf_contents')
    gallery = GallerySerializer(source='galleries', many=True)

    class Meta:
        model = Menu
        fields = ('id', 'href', 'title', 'post', 'information_content', 'gallery', 'parent', 'children', 'is_active')
        extra_kwargs = {
            'children': {'read_only': True},
        }

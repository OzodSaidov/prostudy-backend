from django.core import validators

from django.contrib.auth.models import AbstractUser
from django.contrib import admin
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from prostudy import settings
from prostudy.base_models import Base
from .services.validators import validate_phone, validate_file_type, validate_image_type
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True, verbose_name=_('username'))
    email = models.EmailField(verbose_name=_('email'), blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.get_username()

    @property
    def full_name(self):
        return self.get_full_name()


class Menu(MPTTModel):
    href = models.CharField(max_length=200, null=True, verbose_name='uri')
    title = models.JSONField(default=dict)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        if settings.LANGUAGE_CODE == 'uz':
            return self.title['uz']
        elif settings.LANGUAGE_CODE == 'ru':
            return self.title['ru']
        else:
            return self.title['en']

    class Meta:
        ordering = ['id']


class Post(Base):
    title = models.JSONField(null=True, blank=True, default=dict)
    content = models.JSONField(null=True, blank=True, default=dict)
    url = models.URLField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    short_content = models.JSONField(null=True, blank=True, default=dict)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)


class PostAttachment(Base):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='post_attachments/')


class PostImage(Base):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    file = models.ImageField(upload_to='post_images/', validators=[validate_image_type])
    is_active = models.BooleanField(default=False)


class FileQuerySet(models.QuerySet):
    def delete(self, *args, **kwargs):
        for obj in self:
            obj.file.delete()
        super(FileQuerySet, self).delete()


class Gallery(Base):
    title = models.JSONField(default=dict)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='gallery_files', null=True)
    menu = models.ForeignKey('Menu', on_delete=models.DO_NOTHING, related_name='gallery')

    def __str__(self):
        return self.course.get_category_display()


class GalleryFile(Base):

    def gallery_file_path(self, filename):
        return 'gallery/{0}/{1}'.format(self.gallery.course.get_category_display(), filename)

    file = models.FileField(upload_to=gallery_file_path, validators=[validate_file_type])
    gallery = models.ForeignKey('Gallery', on_delete=models.CASCADE, related_name='gallery_files')
    objects = FileQuerySet.as_manager()

    def __str__(self):
        return self.file.name


"""Предподаватель"""


class Teacher(Base):
    first_name = models.JSONField(default=dict)
    last_name = models.JSONField(default=dict)
    specialty = models.JSONField(default=dict)
    experience = models.JSONField(default=dict)
    photo = models.ImageField(upload_to='teachers/', validators=[validate_image_type])
    menu = models.ForeignKey('Menu', on_delete=models.DO_NOTHING, related_name='teacher')

    def __str__(self):
        return f"{self.first_name['ru']} {self.last_name['ru']}"

    @admin.display(description='Fullname')
    def fullname(self):
        return f"{self.first_name['ru']} {self.last_name['ru']}"


"""Курс"""


class Course(Base):
    GRAPHIC_DESIGN = 1
    WEB_DESIGN = 2
    CMM = 3
    FRONT_END = 4
    BACK_END = 5
    BUSINESS = 6
    LOGO_MAKING = 7
    MICROSOFT_OFFICE = 8
    SOCIAL_MEDIA_MARKETING = 9

    CATEGORY = (
        (GRAPHIC_DESIGN, 'Graphic design'),
        (WEB_DESIGN, 'Web design'),
        (CMM, 'CMM'),
        (FRONT_END, 'Front-end'),
        (BACK_END, 'Back-end'),
        (BUSINESS, 'Business course'),
        (LOGO_MAKING, 'Logo making'),
        (MICROSOFT_OFFICE, 'Microsoft office'),
        (SOCIAL_MEDIA_MARKETING, 'Social Media Marketing'),
    )
    category = models.IntegerField(choices=CATEGORY)
    title = models.JSONField(default=dict)
    href = models.CharField(max_length=200, null=True, verbose_name='uri')
    content = models.JSONField(default=dict, null=True)
    # image_course = models.ImageField(upload_to='courses/', validators=[validate_image_type])
    lesson = models.JSONField(default=dict)
    # lesson_icon = models.ImageField(upload_to='lesson_icon/', validators=[validate_image_type])
    price = models.JSONField(default=dict)
    menu = models.ForeignKey('Menu', on_delete=models.DO_NOTHING, related_name='course')

    def __str__(self):
        return self.get_category_display()

    class Meta:
        ordering = ['id']


class CourseFile(Base):
    def course_file_path(self, filename):
        title = str(self.course.title['en']).replace(' ', '_').lower()
        return 'course_files/{0}/{1}'.format(title, filename)

    course_file = models.FileField(upload_to=course_file_path, validators=[validate_file_type], null=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='course_files')

    def __str__(self):
        return self.course_file.url


class LessonIcon(Base):
    def lesson_icon_path(self, filename):
        title = str(self.course.title['en']).replace(' ', '_').lower()
        return 'lesson_icon/{0}/{1}'.format(title, filename)

    lesson_icon = models.FileField(upload_to=lesson_icon_path, validators=[validate_file_type], null=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='lesson_icons')

    def __str__(self):
        return self.course.get_category_display()


class Program(Base):
    title = models.JSONField(default=dict)
    content = models.JSONField(default=dict)
    image = models.ImageField(upload_to='programs/', validators=[validate_image_type])
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='programs')


"""Рекламный пост"""


class Advertisement(Base):
    title = models.JSONField(default=dict)
    content = models.JSONField(default=dict)
    short_content = models.JSONField(default=dict)
    image_poster = models.ImageField(upload_to='advertisement/', validators=[validate_image_type])
    is_active = models.BooleanField(default=False)
    menu = models.ForeignKey('Menu', on_delete=models.DO_NOTHING, related_name='advertising_post')


"""Обратная связь"""


class Feedback(Base):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=13, validators=[validate_phone])
    message = models.TextField()
    is_active = models.BooleanField(default=True)
    menu = models.ForeignKey('Menu', on_delete=models.DO_NOTHING, related_name='feedback')

    class Meta:
        ordering = ['-create_at']


"""Заявка на подписку"""


class SubscriptionRequest(Base):
    name = models.CharField(max_length=50)
    number_visitors = models.IntegerField()
    phone = models.CharField(max_length=13, validators=[validate_phone])
    is_active = models.BooleanField(default=True)
    menu = models.ForeignKey('Menu', on_delete=models.DO_NOTHING, related_name='subscription')

    class Meta:
        ordering = ['-create_at']


class Company(Base):

    def company_icon_path(self, filename):
        return 'company/{0}/{1}'.format(self.title.lower(), filename)

    title = models.CharField(max_length=200)
    url = models.URLField(validators=[validators.URLValidator(schemes=['https', 'http'])])
    logo = models.ImageField(upload_to=company_icon_path, validators=[validate_image_type])
    menu = models.ForeignKey(Menu, on_delete=models.DO_NOTHING, related_name='companies')

    def __str__(self):
        return self.title

from django.contrib.auth.models import AbstractUser
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from imagekit.processors import ResizeToFit
from imagekit.models import ProcessedImageField

from prostudy import settings
from prostudy.base_models import Base
from .services.validators import validate_phone, validate_file_type_gallery, validate_image_type
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
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='gallery_files')
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, related_name='gallery')

    def __str__(self):
        return self.course.get_category_display()

class GalleryFile(Base):
    file = models.FileField(upload_to='gallery/', validators=[validate_file_type_gallery])
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
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, related_name='teacher')


"""Курс"""
class Course(Base):
    GRAPHIC_DESIGN = 1
    WEB_DESIGN = 2
    CMM = 3
    FRONT_END = 4
    BACK_END = 5

    CATEGORY = (
        (GRAPHIC_DESIGN, 'Graphic design'),
        (WEB_DESIGN, 'Web design'),
        (CMM, 'CMM'),
        (FRONT_END, 'Front-end'),
        (BACK_END, 'Back-end'),
    )
    category = models.IntegerField(choices=CATEGORY)
    title = models.JSONField(default=dict)
    content = models.JSONField(default=dict, null=True)
    # image_course = models.ImageField(upload_to='courses/', validators=[validate_image_type])
    lesson = models.JSONField(default=dict)
    # lesson_icon = models.ImageField(upload_to='lesson_icon/', validators=[validate_image_type])
    price = models.JSONField(default=dict)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, related_name='course')

    def __str__(self):
        return self.get_category_display()


class CourseImage(Base):
    course_image = models.ImageField(upload_to='course_images/', validators=[validate_image_type])
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='course_images')


class LessonIcon(Base):
    lesson_icon = models.ImageField(upload_to='lesson_icons/', validators=[validate_image_type])
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='lesson_icons')


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
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, related_name='advertising_post')


"""Обратная связь"""
class Feedback(Base):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=13, validators=[validate_phone])
    message = models.TextField()
    is_active = models.BooleanField(default=True)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, related_name='feedback')


"""Заявка на подписку"""
class SubscriptionRequisition(Base):
    name = models.CharField(max_length=50)
    number_visitors = models.IntegerField()
    phone = models.CharField(max_length=13, validators=[validate_phone])
    is_active = models.BooleanField(default=True)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, related_name='subscription')

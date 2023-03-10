from django.core import validators
from autoslug import AutoSlugField
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
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, blank=True, related_name='posts')
    course = models.ForeignKey('Course', on_delete=models.CASCADE, null=True, blank=True, related_name='posts')
    program = models.ForeignKey('Program', on_delete=models.CASCADE, null=True, blank=True, related_name='posts')
    is_active = models.BooleanField(default=True)


# class PostAttachment(Base):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='attachments')
#     file = models.FileField(upload_to='post_attachments/')


class PostImage(Base):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    file = models.ImageField(upload_to='post_images/', validators=[validate_image_type])
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.file.url


class FileQuerySet(models.QuerySet):
    def delete(self, *args, **kwargs):
        for obj in self:
            obj.src.delete()
            obj.thumbnail.delete()
        super(FileQuerySet, self).delete()


class Gallery(Base):
    title = models.CharField(max_length=100, null=True)
    course = models.OneToOneField('Course', on_delete=models.CASCADE, null=True, blank=True,
                                  related_name='galleries')
    menu = models.ForeignKey('Menu', on_delete=models.DO_NOTHING, related_name='galleries',
                             null=True, blank=True)

    def __str__(self):
        if self.course:
            return self.course.get_category_display()
        else:
            return self.title


class GalleryFile(Base):

    def gallery_file_path(self, filename):
        title = self.gallery.title.replace(' ', '_').replace('-', '_').lower()
        return 'gallery/{0}/{1}'.format(title, filename)

    title = models.CharField(max_length=100, null=True)
    src = models.FileField(upload_to=gallery_file_path, validators=[validate_file_type])
    thumbnail = models.ImageField(upload_to=gallery_file_path, validators=[validate_image_type],
                                  null=True, blank=True)
    gallery = models.ForeignKey('Gallery', on_delete=models.CASCADE, related_name='gallery_files')
    objects = FileQuerySet.as_manager()


class MainTitle(Base):
    title = models.JSONField(default=dict)
    course = models.OneToOneField('Course', on_delete=models.CASCADE, related_name='titles', null=True, blank=True)
    program = models.OneToOneField('Program', on_delete=models.CASCADE, related_name='titles', null=True, blank=True)


"""????????????????????????????"""


class Teacher(Base):
    def get_populate_from(self):
        return '%s-%s' % (self.first_name['en'], self.last_name['en'])

    first_name = models.JSONField(default=dict)
    last_name = models.JSONField(default=dict)
    specialty = models.JSONField(default=dict)
    experience = models.JSONField(default=dict)
    about = models.JSONField(default=dict)
    information = models.JSONField(default=dict, null=True)
    slug = AutoSlugField(populate_from=get_populate_from, null=True)
    photo = models.ImageField(upload_to='teachers/', validators=[validate_image_type])
    background = models.ImageField(upload_to='teachers/', validators=[validate_image_type], null=True)
    course = models.ForeignKey('Course', on_delete=models.DO_NOTHING, related_name='teachers', null=True)
    menu = models.ForeignKey('Menu', on_delete=models.DO_NOTHING, related_name='teachers')

    def __str__(self):
        return f"{self.first_name['ru']} {self.last_name['ru']}"

    @admin.display(description='Fullname')
    def fullname(self):
        return f"{self.first_name['ru']} {self.last_name['ru']}"

    @property
    def get_teacher_short_info(self):
        return {"name": self.first_name,
                "specialty": self.specialty,
                "photo": self.photo.url}


"""????????"""


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

    def get_populate_from(self):
        return '%s' % (self.get_category_display())

    category = models.IntegerField(choices=CATEGORY)
    title = models.JSONField(default=dict)
    href = models.CharField(max_length=200, null=True, verbose_name='uri')
    slug = AutoSlugField(populate_from=get_populate_from, null=True)
    background = models.ImageField(upload_to='background/', validators=[validate_image_type], null=True)
    menu = models.ForeignKey('Menu', on_delete=models.DO_NOTHING, related_name='courses')

    def __str__(self):
        return self.get_category_display()

    @property
    def get_value(self):
        return self.title['en']

    class Meta:
        ordering = ['id']


class QuestionAndAnswer(Base):
    title = models.JSONField(default=dict, null=True, blank=True)
    description = models.JSONField(default=dict)
    full_description = models.JSONField(default=dict)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='programs_training',
                               null=True, blank=True)
    program = models.ForeignKey('Program', on_delete=models.CASCADE, related_name='questions',
                                null=True, blank=True)


class Result(Base):
    title = models.JSONField(default=dict)
    content = models.JSONField(default=dict)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='results')


class Certificate(Base):
    title = models.JSONField(default=dict, null=True)
    image = models.ImageField(upload_to='certificate/',
                              validators=[validate_image_type])
    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name='cert')


class InformationContent(Base):
    title = models.JSONField(default=dict)
    body = models.JSONField(default=dict)
    background = models.ImageField(upload_to='information_content', null=True, blank=True,
                                   validators=[validate_image_type])
    course = models.OneToOneField(Course, on_delete=models.CASCADE, null=True, blank=True,
                                  related_name='inf_contents')
    program = models.OneToOneField('Program', on_delete=models.CASCADE, null=True, blank=True,
                                   related_name='inf_contents')
    menu = models.OneToOneField(Menu, on_delete=models.CASCADE, null=True, blank=True,
                                related_name='inf_contents')

    def __str__(self):
        return self.title['ru']


class InformationContentDetail(Base):
    title = models.JSONField(default=dict)
    body = models.JSONField(default=dict)
    image = models.FileField(upload_to='course_info_detail/')
    information_content = models.ForeignKey(InformationContent, on_delete=models.CASCADE,
                                            related_name='content_details')


# ?????????????????? ????????????????
class CostOfEducation(Base):
    title = models.JSONField(default=dict)
    body = models.JSONField(default=dict)
    old_price = models.JSONField(default=dict, null=True)
    new_price = models.JSONField(default=dict)
    image = models.FileField(upload_to='cost_education/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='cost_educations')


class CourseFile(Base):
    def course_file_path(self, filename):
        title = str(self.course.title['en']).replace(' ', '_').lower()
        return 'course_files/{0}/{1}'.format(title, filename)

    course_file = models.FileField(upload_to=course_file_path, validators=[validate_file_type], null=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='course_files')

    def __str__(self):
        return self.course_file.url


class Program(Base):
    def get_populate_from(self):
        return '%s' % (self.title['en'])

    title = models.JSONField(default=dict)
    slug = AutoSlugField(populate_from=get_populate_from, null=True)
    image = models.ImageField(upload_to='program/', validators=[validate_image_type], null=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='programs', null=True)

    def __str__(self):
        return self.title['en']


"""?????????????????? ????????"""


class Advertisement(Base):
    def get_populate_from(self):
        return '%s' % (self.title['en'])

    title = models.JSONField(default=dict)
    content = models.JSONField(default=dict)
    image_poster = models.ImageField(upload_to='rek_file/', validators=[validate_image_type])
    is_active = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from=get_populate_from, null=True)
    url = models.URLField(null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='advertising_posts', null=True)


"""???????????????? ??????????"""


class Feedback(Base):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=13, validators=[validate_phone])
    message = models.TextField(null=True, blank=True)
    region = models.CharField(max_length=50, null=True, blank=True)
    course = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-create_at']


"""???????????? ???? ????????????????"""


class SubscriptionRequest(Base):
    name = models.CharField(max_length=50)
    number_visitors = models.IntegerField()
    phone = models.CharField(max_length=13, validators=[validate_phone])
    course = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)

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


class AboutUs(Base):
    image = models.ImageField(upload_to='about_us/', validators=[validate_image_type])
    content = models.JSONField(default=dict)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='abouts', null=True, blank=True)


class Language(Base):
    short_name = models.CharField(max_length=3)
    long_name = models.CharField(max_length=50)


class LifeHack(Base):
    context = models.JSONField(default=dict)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='life_hacks')
    is_active = models.BooleanField(default=True)


class Contact(Base):
    location = models.JSONField(default=dict)
    phone = models.CharField(max_length=13, validators=[validate_phone])
    email = models.EmailField()


class Social(Base):
    title = models.CharField(max_length=50)
    url = models.URLField()
    image = models.ImageField(upload_to='social', validators=[validate_image_type])
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='socials', null=True)


class Presentation(Base):
    file = models.FileField(upload_to='presentation')


class Graduate(Base):
    full_name = models.JSONField(default=dict)
    src = models.URLField(validators=[validators.URLValidator(schemes=['https', 'http'])], null=True)
    video = models.FileField(upload_to='graduate/', null=True)
    thumb = models.ImageField(upload_to='graduate/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='graduates')

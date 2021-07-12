from django.contrib import admin
from django.db import models as dj_models
from django_json_widget.widgets import JSONEditorWidget

from user import models


class BaseAdmin(admin.ModelAdmin):
    formfield_overrides = {
        dj_models.JSONField: {'widget': JSONEditorWidget}
    }


class MenuAdmin(BaseAdmin):
    list_display = ('id', 'title')


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email',)


class CourseAdmin(BaseAdmin):
    list_display = ('category', 'id')


class GalleryFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'src', 'thumbnail', 'gallery')


class CourseFileAdmin(admin.ModelAdmin):
    list_display = ('course', 'course_file')


class TeacherAdmin(BaseAdmin):
    list_display = ('fullname', 'specialty', 'experience', 'course')


class InformationContentAdmin(BaseAdmin):
    list_display = ('id', 'title', 'body', 'background', 'course', 'program', 'menu',)


class CertificateAdmin(BaseAdmin):
    list_display = ('id', 'title', 'image', 'course')


class GalleryAdmin(BaseAdmin):
    list_display = ('id', 'title', 'course', 'menu')


class InformationContentDetailAdmin(BaseAdmin):
    list_display = ('id', 'title', 'body', 'image', 'information_content')


class CostOfEducationAdmin(BaseAdmin):
    list_display = ('id', 'title', 'body', 'old_price', 'new_price', 'image', 'course')


class QuestionAndAnswerAdmin(BaseAdmin):
    list_display = ('id', 'title', 'description', 'full_description', 'program', 'course')


class ResultAdmin(BaseAdmin):
    list_display = ('id', 'title', 'content', 'course')


class PostAdmin(BaseAdmin):
    list_display = ('id', 'title', 'content', 'short_content', 'url', 'slug', 'menu', 'program', 'course', 'is_active')


class AdvertisementAdmin(BaseAdmin):
    list_display = ('id', 'title', 'content', 'image_poster', 'url', 'is_active')


class ProgramAdmin(BaseAdmin):
    list_display = ('id', 'title', 'image', 'course')


class AboutUsAdmin(BaseAdmin):
    list_display = ('id', 'content', 'image')


class ContactAdmin(BaseAdmin):
    list_display = ('id', 'location', 'phone', 'email')


class SocialAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url', 'image')


admin.site.register(models.Menu, MenuAdmin)
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Gallery, GalleryAdmin)
admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.InformationContent, InformationContentAdmin)
admin.site.register(models.InformationContentDetail, InformationContentDetailAdmin)
admin.site.register(models.CostOfEducation, CostOfEducationAdmin)
admin.site.register(models.QuestionAndAnswer, QuestionAndAnswerAdmin)
admin.site.register(models.Result, ResultAdmin)
admin.site.register(models.Certificate, CertificateAdmin)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Teacher, TeacherAdmin)
admin.site.register(models.Advertisement, AdvertisementAdmin)
admin.site.register(models.Program, ProgramAdmin)
admin.site.register(models.GalleryFile, GalleryFileAdmin)
admin.site.register(models.CourseFile, CourseFileAdmin)
admin.site.register(models.AboutUs, AboutUsAdmin)
admin.site.register(models.PostImage)
# admin.site.register(PostAttachment)
admin.site.register(models.Feedback)
admin.site.register(models.SubscriptionRequest)
admin.site.register(models.Company)
admin.site.register(models.Language)
admin.site.register(models.LifeHack, BaseAdmin)
admin.site.register(models.MainTitle, BaseAdmin)
admin.site.register(models.Contact, ContactAdmin)
admin.site.register(models.Social, SocialAdmin)
admin.site.register(models.Presentation)

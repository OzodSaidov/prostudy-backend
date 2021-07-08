from django.contrib import admin
from .models import (
    User,
    PostImage,
    Feedback,
    Gallery,
    GalleryFile,
    Teacher,
    Advertisement,
    SubscriptionRequest,
    # PostAttachment,
    Course,
    InformationContent,
    InformationContentDetail,
    CostOfEducation,
    QuestionAndAnswer,
    Result,
    Certificate,
    Menu,
    Post,
    Program,
    CourseFile,
    Company,
    QuestionTitle,
)


class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email',)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('category', 'id')


class GalleryFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'image_for_video', 'gallery')


class CourseFileAdmin(admin.ModelAdmin):
    list_display = ('course', 'course_file')


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'specialty', 'experience')


class InformationContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(User, UserAdmin)
admin.site.register(Gallery)
admin.site.register(Course, CourseAdmin)
admin.site.register(InformationContent, InformationContentAdmin)
admin.site.register(InformationContentDetail)
admin.site.register(CostOfEducation)
admin.site.register(QuestionAndAnswer)
admin.site.register(Result)
admin.site.register(Certificate)
admin.site.register(Post)
admin.site.register(PostImage)
# admin.site.register(PostAttachment)
admin.site.register(Feedback)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Advertisement)
admin.site.register(SubscriptionRequest)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Program)
admin.site.register(GalleryFile, GalleryFileAdmin)
admin.site.register(CourseFile, CourseFileAdmin)
admin.site.register(Company)
admin.site.register(QuestionTitle)

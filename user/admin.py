from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email',)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('category', 'id')


class GalleryFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'id', 'gallery')


class CourseFileAdmin(admin.ModelAdmin):
    list_display = ('course', 'course_file')


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'specialty', 'experience')


admin.site.register(User, UserAdmin)
admin.site.register(Gallery)
admin.site.register(Course, CourseAdmin)
admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(PostAttachment)
admin.site.register(Feedback)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Advertisement)
admin.site.register(SubscriptionRequest)
admin.site.register(Menu)
admin.site.register(Program)
admin.site.register(GalleryFile, GalleryFileAdmin)
admin.site.register(CourseFile, CourseFileAdmin)
admin.site.register(LessonIcon)

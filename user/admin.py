from django.contrib import admin
from .models import (
    User,
    PostImage,
    Feedback,
    Gallery,
    GalleryFile,
    Teacher,
    Advertisement,
    SubscriptionRequisition,
    PostAttachment,
    Course,
    Menu,
    Post,
    Program,
    CourseImage,
    LessonIcon,
)


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email',)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')


admin.site.register(User, UserAdmin)
admin.site.register(Gallery)
admin.site.register(Course, CourseAdmin)
admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(PostAttachment)
admin.site.register(Feedback)
admin.site.register(Teacher)
admin.site.register(Advertisement)
admin.site.register(SubscriptionRequisition)
admin.site.register(Menu)
admin.site.register(Program)
admin.site.register(GalleryFile)
admin.site.register(CourseImage)
admin.site.register(LessonIcon)

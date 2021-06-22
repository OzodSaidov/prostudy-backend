from django.contrib import admin
from .models import (
    User,
    PostImage,
    Feedback,
    GalleryFile,
    Teacher,
    Advertisement,
    SubscriptionRequisition,
    PostAttachment,
    Course,
    Menu,
    Post,
    Program
)


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email',)


class GalleryFileAdmin(admin.ModelAdmin):
    list_display = ('file',)

    def get_files(self, obj):
        return obj.file

    get_files.short_description = 'Files'


admin.site.register(User, UserAdmin)
admin.site.register(GalleryFile, GalleryFileAdmin)
admin.site.register(Course)
admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(PostAttachment)
admin.site.register(Feedback)
admin.site.register(Teacher)
admin.site.register(Advertisement)
admin.site.register(SubscriptionRequisition)
admin.site.register(Menu)
admin.site.register(Program)


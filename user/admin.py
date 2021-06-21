from django.contrib import admin
from .models import (
    User,
    PostImage,
    Feedback,
    Graduate,
    Comment,
    Gallery,
    GalleryFile,
    Teacher,
    Specialty,
    Advertisement,
    SubscriptionRequisition,
    PostAttachment,
    Course,
    Menu,
    Post,
    Review,
)


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email',)


class GalleryFileAdmin(admin.ModelAdmin):
    list_display = ('gallery', 'file')

    def get_files(self, obj):
        return obj.file
    get_files.short_description = 'Files'


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('category', )


admin.site.register(User, UserAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryFile, GalleryFileAdmin)
admin.site.register(Course)
admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(PostAttachment)
admin.site.register(Graduate)
admin.site.register(Comment)
admin.site.register(Feedback)
admin.site.register(Teacher)
admin.site.register(Specialty)
admin.site.register(Advertisement)
admin.site.register(SubscriptionRequisition)
admin.site.register(Menu)
admin.site.register(Review)

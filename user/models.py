from django.contrib.auth.models import AbstractUser
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from prostudy.base_models import Base
from .services.validators import validate_phone


class User(AbstractUser):
    pass

    def __str__(self):
        return self.get_username()

    @property
    def full_name(self):
        return self.get_full_name()


# class Notification(Base):
#     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent')
#     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received')
#     text = models.TextField()
#     is_read = models.BooleanField(default=False)


class Menu(MPTTModel):
    title = models.JSONField(default=dict)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    is_active = models.BooleanField(default=False)


class Post(Base):
    title = models.JSONField(null=True, blank=True, default=dict)
    content = models.JSONField(null=True, blank=True, default=dict)
    url = models.URLField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    short_content = models.JSONField(null=True, blank=True, default=dict)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)


class Comment(MPTTModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    content = models.TextField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)


class PostAttachment(Base):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='post_attachments/')


class PostImage(Base):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    file = models.ImageField(upload_to='post_images/')
    is_active = models.BooleanField(default=False)


class Gallery(Base):
    GRAPHIC_DESIGN = 1
    WEB_DESIGN = 2
    CMM = 3

    CATEGORY = (
        (GRAPHIC_DESIGN, 'Graphic design'),
        (WEB_DESIGN, 'Web design'),
        (CMM, 'CMM')
    )

    category = models.IntegerField(choices=CATEGORY)
    file = models.FileField(upload_to='gallery/')


"""Предподаватель"""
class Teacher(Base):
    first_name = models.JSONField(default=dict)
    last_name = models.JSONField(default=dict)
    photo = models.ImageField(upload_to='teachers/')


"""Специальност"""
class Specialty(Base):
    title = models.JSONField(default=dict)
    content = models.JSONField(default=dict)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)


"""Выпускник"""
class Graduate(Base):
    first_name = models.JSONField(default=dict)
    last_name = models.JSONField(default=dict)
    photo = models.ImageField(upload_to='graduates/')


"""Курс"""
class Course(Base):
    title = models.JSONField(default=dict)
    short_title = models.JSONField(default=dict)
    content = models.JSONField(default=dict)
    short_content = models.JSONField(default=dict)
    image_poster = models.ImageField(upload_to='courses/')
    graduate = models.ForeignKey(Graduate, on_delete=models.DO_NOTHING)
    gallery = models.OneToOneField(Gallery, on_delete=models.DO_NOTHING)


"""Рекламный пост"""
class Advertisement(Base):
    title = models.JSONField(default=dict)
    content = models.JSONField(default=dict)
    short_content = models.JSONField(default=dict)
    image_poster = models.ImageField(upload_to='advertisement/')
    is_active = models.BooleanField(default=False)


"""Отзыв"""
class Review(Base):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    is_active = models.BooleanField(default=False)


"""Обратная связь"""
class Feedback(Base):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.FloatField(validators=[validate_phone])
    message = models.TextField()


"""Заявка на подписку"""
class SubscriptionRequisition(Base):
    name = models.CharField(max_length=50)
    number_visitors = models.IntegerField()
    phone = models.FloatField(validators=[validate_phone])

# ===========================================

# def send_review_notification(review_id: int):
#     from application.models import ApplicationReview
#     review = ApplicationReview.objects.get(id=review_id)
#     receiver = review.application.user
#     sender = review.commission_member.user
#     text = dict({"is_passed": review.is_passed, "public_id": review.application.public_id,
#                  "refusal_reason": {review.refusal_reason}, "review_budget": review.review_budget})
#     Notification.objects.create(receiver=receiver, sender=sender, text=text)

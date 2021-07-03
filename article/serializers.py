from rest_framework import serializers

from .models import *


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    body = serializers.CharField()
    author_id = serializers.IntegerField()
    created_at = serializers.DateTimeField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.author_id = validated_data.get('author_id', instance.author_id)
        instance.save()
        return instance

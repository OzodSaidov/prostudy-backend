from rest_framework import serializers

from .models import *


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    body = serializers.CharField()
    author_id = serializers.IntegerField()
    created_at = serializers.DateTimeField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

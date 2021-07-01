from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *


class AricleView(APIView):
    def get(self, request):
        serializer = ArticleSerializer(Article.objects.all(), many=True)
        return Response({'aricles': serializer.data})

    def post(self, request):
        article = request.data.get('article')
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            saved_article = serializer.save()
        return Response({'success': f'Article \"{saved_article.title}\" created successfully'})

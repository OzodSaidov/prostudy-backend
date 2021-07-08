# from rest_framework.views import APIView
# from rest_framework.generics import get_object_or_404
# from rest_framework.response import Response
from rest_framework import generics
from rest_framework import request

from .serializers import *


# class AricleView(APIView):
#     def get(self, request, pk=None):
#         if pk:
#             article = get_object_or_404(Article.objects.all(), pk=pk)
#             serializer = ArticleSerializer(instance=article)
#             return Response(serializer.data)
#         serializer = ArticleSerializer(Article.objects.all(), many=True)
#         return Response({'aricles': serializer.data})
#
#     def post(self, request):
#         article = request.data.get('article')
#         serializer = ArticleSerializer(data=article)
#         if serializer.is_valid(raise_exception=True):
#             saved_article = serializer.save()
#         return Response({'success': f"Article '{saved_article.title}' created successfully"})
#
#     def put(self, request, pk):
#         saved_article = get_object_or_404(Article.objects.all(), pk=pk)
#         data = request.data.get('article')
#         serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             article_saved = serializer.save()
#         return Response({'success': f"Article '{saved_article.title}' edited successfully"})
#
#     def delete(self, request, pk):
#         # Get object with this pk
#         article = get_object_or_404(Article.objects.all(), pk=pk)
#         article.delete()
#         return Response({
#             'message': f'Article with id `{id}` has been deleted'
#         }, status=204)

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

from django.urls import path
# from article.views import AricleView
from article.views import ArticleDetail, ArticleList, AuthorDetail, AuthorList

urlpatterns = [
    path('articles/', ArticleList.as_view()),
    path('articles/<int:pk>', ArticleDetail.as_view()),
    path('authors/', AuthorList.as_view()),
    path('authors/<int:pk>', AuthorDetail.as_view()),
]

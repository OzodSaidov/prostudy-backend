from django.urls import path, include
# from article.views import AricleView
from article.views import ArticleDetail, ArticleList, AuthorDetail, AuthorList
from prostudy import settings

urlpatterns = [
    path('articles/', ArticleList.as_view()),
    path('articles/<int:pk>', ArticleDetail.as_view()),
    path('authors/', AuthorList.as_view()),
    path('authors/<int:pk>', AuthorDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]

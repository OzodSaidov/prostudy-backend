from django.urls import path
from article.views import AricleView

urlpatterns = [
    path('articles/', AricleView.as_view()),
    path('articles/<int:pk>', AricleView.as_view()),
]

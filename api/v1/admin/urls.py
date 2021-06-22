from django.urls import path, include

from api.v1.admin.views import (
    MenuCreateView,
    MenuEditView,
    PostCreateView,
    PostEditView,
    GalleryCreateView,
    GalleryEditView,
)

urlpatterns = [
    path('menu/create/', MenuCreateView.as_view()),
    path('menu/<int:id>/', MenuEditView.as_view()),
    path('post/create/', PostCreateView.as_view()),
    path('post/<int:id>/', PostEditView.as_view()),
    path('gallery/create/', GalleryCreateView.as_view()),
    path('gallery/<int:id>', GalleryEditView.as_view()),
]

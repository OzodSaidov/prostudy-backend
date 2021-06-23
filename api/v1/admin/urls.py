from django.urls import path, include

from api.v1.admin.views import (
    MenuCreateView,
    MenuEditView,
    PostCreateView,
    PostEditView,
    GalleryCreateView,
    GalleryEditView,
    TeacherCreateView,
    TeacherEditView, ProgramCreateView,
    # GraduateCreateView,
    # GraduateEditView,
)

urlpatterns = [
    path('menu/create/', MenuCreateView.as_view()),
    path('menu/<int:id>/', MenuEditView.as_view()),
    path('post/create/', PostCreateView.as_view()),
    path('post/<int:id>/', PostEditView.as_view()),
    path('gallery/create/', GalleryCreateView.as_view()),
    path('gallery/<int:id>', GalleryEditView.as_view()),
    path('teacher/create/', TeacherCreateView.as_view()),
    path('teacher/<int:id>', TeacherEditView.as_view()),
    # path('graduate/create/', GraduateCreateView.as_view()),
    # path('graduate/<int:id>', GraduateEditView.as_view()),
    path('program/create/', ProgramCreateView.as_view())
]

from django.urls import path, include

from api.v1.admin.views import (
    MenuCreateView,
    MenuEditView,
    PostCreateView,
    PostEditView,
    GalleryCreateView,
    GalleryEditView,
    TeacherCreateView,
    TeacherEditView,
    ProgramCreateView,
    CourseCreateView,
    CourseEditView,
    ProgramEditView,
    FeedbackCreateView,
    FeedbackEditView, GalleryFileCreateView, GalleryFileRetrieveDestroyView, SubscriptionRequestCreateView,
    SubscriptionRequestEditView, CourseFileCreateView, CourseFileRetrieveDestroyView, CompanyCreateView,
    CompanyEditView,
)

urlpatterns = [
    path('menu/create/', MenuCreateView.as_view()),
    path('menu/<int:id>/', MenuEditView.as_view()),
    path('post/create/', PostCreateView.as_view()),
    path('post/<int:id>/', PostEditView.as_view()),
    path('gallery/create/', GalleryCreateView.as_view()),
    path('gallery/<int:id>/', GalleryEditView.as_view()),
    path('gallery/file/create/', GalleryFileCreateView.as_view()),
    path('gallery/file/<int:id>/', GalleryFileRetrieveDestroyView.as_view()),
    path('course/create/', CourseCreateView.as_view()),
    path('course/<int:id>/', CourseEditView.as_view()),
    path('course/file/create/', CourseFileCreateView.as_view()),
    path('course/file/<int:id>/', CourseFileRetrieveDestroyView.as_view()),
    path('program/create/', ProgramCreateView.as_view()),
    path('program/<int:id>/', ProgramEditView.as_view()),
    path('teacher/create/', TeacherCreateView.as_view()),
    path('teacher/<int:id>/', TeacherEditView.as_view()),
    path('feedback/create/', FeedbackCreateView.as_view()),
    path('feedback/<int:id>/', FeedbackEditView.as_view()),
    path('subscriptionrequest/create/', SubscriptionRequestCreateView.as_view()),
    path('subscriptionrequest/<int:id>/', SubscriptionRequestEditView.as_view()),
    path('companies/', CompanyCreateView.as_view()),
    path('companies/<int:id>/', CompanyEditView.as_view()),
]
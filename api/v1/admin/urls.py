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
    CompanyEditView, CourseInfoCreateView, CourseInfoEditView, CourseInfoDetailCreateView, CourseInfoDetailEditView,
    CostEducationCreateView, CostEducationEditView, CertificateCreateView, CertificateEditView,
    ProgramTrainingCreateView, ProgramTrainingEditView, ResultCreateView, ResultEditView, CostEducationListByCourseView,
    CourseInfoByCourseView, CertificateByCourseView, ProgramTrainingListByCourseView, ResultListByCourseView,
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


    path('course/<int:id>/information/', CourseInfoByCourseView.as_view()),
    path('course/information/', CourseInfoCreateView.as_view()),
    path('course/information/<int:id>/', CourseInfoEditView.as_view()),


    path('course/info-details/', CourseInfoDetailCreateView.as_view()),
    path('course/info-details/<int:id>/', CourseInfoDetailEditView.as_view()),


    path('course/<int:id>/cost-educations/', CostEducationListByCourseView.as_view()),
    path('course/cost-education/', CostEducationCreateView.as_view()),
    path('course/cost-education/<int:id>/', CostEducationEditView.as_view()),


    path('course/<int:id>/certificate/', CertificateByCourseView.as_view()),
    path('course/certificate/', CertificateCreateView.as_view()),
    path('course/certificate/<int:id>/', CertificateEditView.as_view()),


    path('course/<int:id>/program-training/', ProgramTrainingListByCourseView.as_view()),
    path('course/program-training/', ProgramTrainingCreateView.as_view()),
    path('course/program-training/<int:id>/', ProgramTrainingEditView.as_view()),


    path('course/<int:id>/results/', ResultListByCourseView.as_view()),
    path('course/result/', ResultCreateView.as_view()),
    path('course/result/<int:id>/', ResultEditView.as_view()),
]

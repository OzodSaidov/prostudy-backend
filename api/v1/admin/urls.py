from django.urls import path
from api.v1.admin.views import *

urlpatterns = [
    path('home/', HomeView.as_view()),
    path('lifehacks/', LifeHackView.as_view()),
    path('lifehacks/<int:id>/', LifeHackEditView.as_view()),
    path('languages/', LanguageView.as_view()),
    path('languages/<int:id>', LanguageEditView.as_view()),
    path('menu/create/', MenuCreateView.as_view()),
    path('menu/<int:id>/', MenuEditView.as_view()),
    path('menu/<int:id>/posts/', PostByMenuView.as_view()),
    path('menu/<int:id>/gallery/', GalleryByMenuView.as_view()),
    path('menu/<int:id>/info-content/', InformationContentByMenuView.as_view()),
    path('menu/<int:id>/blog/', MenuBlogView.as_view()),
    path('post/create/', PostCreateView.as_view()),
    path('post/<int:id>/', PostEditView.as_view()),
    path('gallery/create/', GalleryCreateView.as_view()),
    path('gallery/<int:id>/', GalleryEditView.as_view()),
    path('gallery/file/create/', GalleryFileCreateView.as_view()),
    path('gallery/file/<int:id>/', GalleryFileRetrieveDestroyView.as_view()),
    path('course/create/', CourseCreateView.as_view()),
    path('course/result/', ResultCreateView.as_view()),
    path('course/names/', CourseNameView.as_view()),
    path('course/information/', InformationContentCreateView.as_view()),
    path('course/info-details/', InformationContentDetailCreateView.as_view()),
    path('course/cost-education/', CostEducationCreateView.as_view()),
    path('course/certificate/', CertificateCreateView.as_view()),
    path('course/program-training/', QuestionAndAnswersCreateView.as_view()),
    path('course/file/create/', CourseFileCreateView.as_view()),
    path('course/file/<int:id>/', CourseFileRetrieveDestroyView.as_view()),
    path('course/information/<int:id>/', InformationContentEditView.as_view()),
    path('course/info-details/<int:id>/', InformationContentDetailEditView.as_view()),
    path('course/cost-education/<int:id>/', CostEducationEditView.as_view()),
    path('course/certificate/<int:id>/', CertificateEditView.as_view()),
    path('course/program-training/<int:id>/', QuestionAndAnswersEditView.as_view()),
    path('course/result/<int:id>/', ResultEditView.as_view()),
    path('course/<str:slug>/', CourseEditView.as_view()),
    path('course/<str:slug>/programs/', ProgramListByCourseView.as_view()),
    path('course/<str:slug>/teachers/', TeacherListByCourseView.as_view()),
    path('course/<str:slug>/information/', InformationContentByCourseView.as_view()),
    path('course/<str:slug>/cost-educations/', CostEducationListByCourseView.as_view()),
    path('course/<str:slug>/certificate/', CertificateByCourseView.as_view()),
    path('course/<str:slug>/program-training/', QuestionAndAnswersListByCourseView.as_view()),
    path('course/<str:slug>/results/', ResultListByCourseView.as_view()),
    path('course/<str:slug>/informations/', CourseInformationView.as_view()),
    path('program/create/', ProgramCreateView.as_view()),
    path('program/<str:slug>/', ProgramEditView.as_view()),
    path('program/<str:slug>/info-content/', InfoContentByProgramView.as_view()),
    path('program/<str:slug>/question/', QuestionListByProgramView.as_view()),
    path('program/<str:slug>/gallery/', GalleryByProgramView.as_view()),
    path('program/<str:slug>/posts/', PostListByProgramView.as_view()),
    path('program/<str:slug>/informations/', ProgramInformationView.as_view()),
    path('teacher/create/', TeacherCreateView.as_view()),
    path('teacher/<int:id>/', TeacherEditView.as_view()),
    path('feedback/', FeedbackCreateView.as_view()),
    path('feedback/list/', FeedbackView.as_view()),
    path('feedback/<int:id>/', FeedbackEditView.as_view()),
    path('subscriptionrequest/create/', SubscriptionRequestCreateView.as_view()),
    path('subscriptionrequests/', SubscriptionRequestView.as_view()),
    path('subscriptionrequest/<int:id>/', SubscriptionRequestEditView.as_view()),
    path('companies/', CompanyCreateView.as_view()),
    path('companies/<int:id>/', CompanyEditView.as_view()),
    path('main-titles/', MainTitleView.as_view()),
    path('main-titles/<int:id>', MainTitleEditView.as_view()),
    path('contact/', ContactView.as_view()),
    path('contact/<int:id>/', ContactEditView.as_view()),
    path('social/', SocialView.as_view()),
    path('social/<int:id>/', SocialEditView.as_view()),
    path('presentation/', PresentationView.as_view()),
    path('presentation/<int:id>/', PresentationEditView.as_view()),
    path('graduates/', GraduateView.as_view()),
    path('graduates/<int:id>/', GraduateEditView.as_view()),
]

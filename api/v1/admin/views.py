from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView, \
    ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework.throttling import AnonRateThrottle
from api.v1.admin.serializers import *
from region.models import Region
from user.models import *


class PostCreateView(ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()


class PostEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    lookup_url_kwarg = 'id'


class MenuCreateView(ListCreateAPIView):
    serializer_class = MenuSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Menu.objects.filter(parent=None)


class MenuEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = MenuSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Menu.objects.all()
    lookup_url_kwarg = 'id'


class GalleryFileCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = GalleryFileSerializer
    queryset = GalleryFile.objects.all()


class GalleryFileRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = GalleryFile.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = GalleryFileSerializer
    lookup_url_kwarg = 'id'


class GalleryCreateView(ListCreateAPIView):
    serializer_class = GallerySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def get_queryset(self):
        queryset = Gallery.objects.filter(course__category__isnull=False)
        return queryset


class GalleryEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = GallerySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Gallery.objects.all()
    lookup_url_kwarg = 'id'


class GalleryByProgramView(ListAPIView):
    serializer_class = GallerySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        gallery = Gallery.objects.filter(course__programs__slug=self.kwargs['slug'])
        return gallery


class TeacherListByCourseView(ListAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        teachers = Teacher.objects.filter(course__slug=self.kwargs['slug'])
        return teachers


class TeacherCreateView(ListCreateAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Teacher.objects.all()


class TeacherEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Teacher.objects.all()
    lookup_url_kwarg = 'id'


class CourseFileCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CourseFileSerializer
    queryset = CourseFile.objects.all()


class CourseFileRetrieveDestroyView(RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CourseFileSerializer
    queryset = CourseFile.objects.all()
    lookup_url_kwarg = 'id'


class CourseCreateView(ListCreateAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Course.objects.all()


class CourseEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Course.objects.all()
    lookup_field = 'slug'


class ProgramListByCourseView(ListAPIView):
    serializer_class = ProgramSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        programs = Program.objects.filter(course__slug=self.kwargs['slug'])
        return programs


class InfoContentByProgramView(APIView):
    serializer_class = InformationContentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        inf_content = InformationContent.objects.get(program__slug=self.kwargs['slug'])
        return inf_content


class QuestionListByProgramView(APIView):
    serializer_class = QuestionAndAnswersSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        questions = QuestionAndAnswer.objects.filter(program__slug=self.kwargs['slug'])
        return questions


class ProgramCreateView(CreateAPIView):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()
    permission_classes = [IsAuthenticated]


class ProgramEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()
    lookup_field = 'slug'


class AdvertisementCreateView(ListCreateAPIView):
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Advertisement.objects.filter(is_active=True)


class AdvertisementEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Advertisement.objects.all()
    lookup_url_kwarg = 'id'


class FeedbackCreateView(CreateAPIView):
    throttle_classes = [AnonRateThrottle]
    permission_classes = [AllowAny]
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()


class FeedbackView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()


class FeedbackEditView(RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    lookup_url_kwarg = 'id'


class SubscriptionRequestCreateView(CreateAPIView):
    throttle_classes = [AnonRateThrottle]
    permission_classes = [AllowAny]
    serializer_class = SubscriptionRequestSerializer
    queryset = SubscriptionRequest.objects.all()


class SubscriptionRequestView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SubscriptionRequestSerializer
    queryset = SubscriptionRequest.objects.all()


class SubscriptionRequestEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SubscriptionRequestSerializer
    queryset = SubscriptionRequest.objects.all()
    lookup_url_kwarg = 'id'


class CompanyCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class CompanyEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    lookup_url_kwarg = 'id'


class InformationContentByCourseView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = InformationContentSerializer

    def get_queryset(self):
        queryset = InformationContent.objects.get(course__slug=self.kwargs['slug'])
        return queryset


class InformationContentCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = InformationContentSerializer
    queryset = InformationContent.objects.all()


class InformationContentEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = InformationContentSerializer
    queryset = InformationContent.objects.all()
    lookup_url_kwarg = 'id'


class InformationContentDetailCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = InformationContentDetailSerializer
    queryset = InformationContentDetail.objects.all()


class InformationContentDetailEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = InformationContentDetailSerializer
    queryset = InformationContentDetail.objects.all()
    lookup_url_kwarg = 'id'


class CostEducationListByCourseView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CostOfEducationSerializer

    def get_queryset(self):
        education_costs = CostOfEducation.objects.filter(course__slug=self.kwargs['slug'])
        return education_costs


class CostEducationCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CostOfEducationSerializer
    queryset = CostOfEducation.objects.all()


class CostEducationEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CostOfEducationSerializer
    queryset = CostOfEducation.objects.all()
    lookup_url_kwarg = 'id'


class CertificateByCourseView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CertificateSerializer

    def get_queryset(self):
        cert = Certificate.objects.get(course__slug=self.kwargs['slug'])
        return cert


class CertificateCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CertificateSerializer
    queryset = Certificate.objects.all()


class CertificateEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CertificateSerializer
    queryset = Certificate.objects.all()
    lookup_url_kwarg = 'id'


class QuestionAndAnswersListByCourseView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = QuestionAndAnswersSerializer

    def get_queryset(self):
        questions = QuestionAndAnswer.objects.filter(course__slug=self.kwargs['slug'])
        return questions


class QuestionAndAnswersCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionAndAnswersSerializer
    queryset = QuestionAndAnswer.objects.all()


class QuestionAndAnswersEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = QuestionAndAnswersSerializer
    queryset = QuestionAndAnswer.objects.all()
    lookup_url_kwarg = 'id'


class ResultListByCourseView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ResultSerializer

    def get_queryset(self):
        results = Result.objects.filter(course__slug=self.kwargs['slug'])
        return results


class ResultCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ResultSerializer
    queryset = Result.objects.all()


class ResultEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ResultSerializer
    queryset = Result.objects.all()
    lookup_url_kwarg = 'id'


class PostByMenuView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer

    def get_queryset(self):
        posts = Post.objects.filter(menu_id=self.kwargs['id'])
        return posts


class GalleryByMenuView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = GallerySerializer

    def get_queryset(self):
        gallery = Gallery.objects.filter(menu_id=self.kwargs['id'])
        return gallery


class PostListByProgramView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.filter(program__slug=self.kwargs['slug'])
        return queryset


class InformationContentByMenuView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializers = InformationContentSerializer

    def get(self):
        queryset = InformationContent.objects.get(menu_id=self.kwargs['id'])
        return queryset


class CourseInformationView(RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CourseInformationSerializer
    queryset = Course.objects.all()
    lookup_field = 'slug'


class ProgramInformationView(RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProgramInformationSerializer
    queryset = Program.objects.all()
    lookup_field = 'slug'


class MenuBlogView(RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = MenuBlogSerializer
    queryset = Menu.objects.all()
    lookup_url_kwarg = 'id'


class CourseNameView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CourseNameSerializer
    queryset = Course.objects.all()


class LanguageView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()


class LanguageEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()
    lookup_url_kwarg = 'id'


class LifeHackView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = LifeHackSerializer
    queryset = LifeHack.objects.filter(is_active=True)


class LifeHackEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = LifeHackSerializer
    queryset = LifeHack.objects.all()
    lookup_url_kwarg = 'id'


class HomeView(ObjectMultipleModelAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = RegionSerializer
    querylist = [
        {'queryset': Advertisement.objects.filter(is_active=True), 'serializer_class': AdvertisementSerializer},
        {'queryset': Course.objects.all()[:4], 'serializer_class': CourseSerializer},
        {'queryset': AboutUs.objects.filter(menu__isnull=True), 'serializer_class': AboutUsSerializer},
        {'queryset': LifeHack.objects.filter(is_active=True), 'serializer_class': LifeHackSerializer},
        {'queryset': Teacher.objects.all(), 'serializer_class': TeacherSerializer},
        {'queryset': Company.objects.all(), 'serializer_class': CompanySerializer},
        {'queryset': Region.objects.all(), 'serializer_class': serializer_class},
        {'queryset': Presentation.objects.all(), 'serializer_class': PresentationSerializer},
    ]


class MainTitleView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MainTitleSerializer
    queryset = MainTitle.objects.all()


class MainTitleEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = MainTitleSerializer
    queryset = MainTitle.objects.all()
    lookup_url_kwarg = 'id'


class PresentationView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PresentationSerializer
    queryset = Presentation.objects.all()


class PresentationEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PresentationSerializer
    queryset = Presentation.objects.all()
    lookup_url_kwarg = 'id'


class ContactView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    lookup_url_kwarg = 'id'


class SocialView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SocialSerializer
    queryset = Social.objects.all()


class SocialEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SocialSerializer
    queryset = Social.objects.all()
    lookup_url_kwarg = 'id'


class GraduateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GraduateSerializer
    queryset = Graduate.objects.all()


class GraduateEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = GraduateSerializer
    queryset = Graduate.objects.all()
    lookup_field = 'id'

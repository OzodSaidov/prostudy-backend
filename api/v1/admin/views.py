from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView, \
    ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.admin.serializers import *
# from api.v1.admin.services.throttles import PostAnononymousRateThrottle
from user.models import *


class PostCreateView(ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)
    queryset = Post.objects.all()


class PostEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    lookup_url_kwarg = 'id'


class MenuCreateView(ListCreateAPIView):
    serializer_class = MenuSerializer
    permission_classes = (AllowAny,)
    queryset = Menu.objects.filter(parent=None)


class MenuEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = MenuSerializer
    permission_classes = (AllowAny,)
    queryset = Menu.objects.all()
    lookup_url_kwarg = 'id'


class GalleryFileCreateView(ListCreateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = GalleryFileSerializer
    queryset = GalleryFile.objects.all()


class GalleryFileRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = GalleryFile.objects.all()
    permission_classes = [AllowAny]
    serializer_class = GalleryFileSerializer
    lookup_url_kwarg = 'id'


class GalleryCreateView(ListCreateAPIView):
    serializer_class = GallerySerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        queryset = Gallery.objects.filter(course__category__isnull=False)
        return queryset


class GalleryEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = GallerySerializer
    permission_classes = [AllowAny, ]
    queryset = Gallery.objects.all()
    lookup_url_kwarg = 'id'


class GalleryByProgramView(ListAPIView):
    serializer_class = GallerySerializer
    permission_classes = [AllowAny]
    queryset = Gallery.objects.all()

    def get_queryset(self):
        gallery = Gallery.objects.filter(course__programs=self.kwargs['id'])
        return gallery


class TeacherListByCourseView(ListAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        teachers = Teacher.objects.filter(course_id=self.kwargs['id'])
        return teachers


class TeacherCreateView(ListCreateAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny, ]
    queryset = Teacher.objects.all()


class TeacherEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny, ]
    queryset = Teacher.objects.all()
    lookup_url_kwarg = 'id'


class CourseFileCreateView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CourseFileSerializer
    queryset = CourseFile.objects.all()


class CourseFileRetrieveDestroyView(RetrieveDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = CourseFileSerializer
    queryset = CourseFile.objects.all()
    lookup_url_kwarg = 'id'


class CourseCreateView(ListCreateAPIView):
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]
    queryset = Course.objects.all()


class CourseEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]
    queryset = Course.objects.all()
    lookup_url_kwarg = 'id'


class ProgramListByCourseView(ListAPIView):
    serializer_class = ProgramSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        programs = Program.objects.filter(course_id=self.kwargs['id'])
        return programs


class InfoContentByProgramView(APIView):
    serializer_class = InformationContentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        inf_content = InformationContent.objects.get(program_id=self.kwargs['id'])
        return inf_content


class QuestionListByProgramView(APIView):
    serializer_class = QuestionAndAnswersSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        questions = QuestionAndAnswer.objects.filter(program_id=self.kwargs['id'])
        return questions


class ProgramCreateView(CreateAPIView):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()
    permission_classes = [AllowAny]


class ProgramEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()
    lookup_url_kwarg = 'id'


class AdvertisementCreateView(ListCreateAPIView):
    serializer_class = AdvertisementSerializer
    permission_classes = [AllowAny]
    queryset = Advertisement.objects.filter(is_active=True)


class AdvertisementEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = AdvertisementSerializer
    permission_classes = [AllowAny]
    queryset = Advertisement.objects.all()
    lookup_url_kwarg = 'id'


class FeedbackCreateView(CreateAPIView):
    # throttle_classes = [PostAnononymousRateThrottle, ]
    permission_classes = [AllowAny]
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()


class FeedbackEditView(RetrieveDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    lookup_url_kwarg = 'id'


class SubscriptionRequestCreateView(ListCreateAPIView):
    # throttle_classes = [PostAnononymousRateThrottle]
    permission_classes = [AllowAny]
    serializer_class = SubscriptionRequestSerializer
    queryset = SubscriptionRequest.objects.all()


class SubscriptionRequestEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = SubscriptionRequestSerializer
    queryset = SubscriptionRequest.objects.all()
    lookup_url_kwarg = 'id'


class CompanyCreateView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class CompanyEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    lookup_url_kwarg = 'id'


class InformationContentByCourseView(APIView):
    permission_classes = [AllowAny]
    serializer_class = InformationContentSerializer

    def get(self, request, *args, **kwargs):
        queryset = InformationContent.objects.get(course_id=self.kwargs['id'])
        serializer = InformationContentSerializer(queryset)
        return Response(serializer.data)


class InformationContentCreateView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = InformationContentSerializer
    queryset = InformationContent.objects.all()


class InformationContentEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = InformationContentSerializer
    queryset = InformationContent.objects.all()
    lookup_url_kwarg = 'id'


class InformationContentDetailCreateView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = InformationContentDetailSerializer
    queryset = InformationContentDetail.objects.all()


class InformationContentDetailEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = InformationContentDetailSerializer
    queryset = InformationContentDetail.objects.all()
    lookup_url_kwarg = 'id'


class CostEducationListByCourseView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CostOfEducationSerializer

    def get_queryset(self):
        education_costs = CostOfEducation.objects.filter(course_id=self.kwargs['id'])
        return education_costs


class CostEducationCreateView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CostOfEducationSerializer
    queryset = CostOfEducation.objects.all()


class CostEducationEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = CostOfEducationSerializer
    queryset = CostOfEducation.objects.all()
    lookup_url_kwarg = 'id'


class CertificateByCourseView(APIView):
    permission_classes = [AllowAny]
    serializer_class = CertificateSerializer
    queryset = Certificate.objects.all()

    def get(self, request, *args, **kwargs):
        cert = Certificate.objects.get(course_id=self.kwargs['id'])
        serializer = CertificateSerializer(cert)
        return Response(serializer.data)


class CertificateCreateView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CertificateSerializer
    queryset = Certificate.objects.all()


class CertificateEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = CertificateSerializer
    queryset = Certificate.objects.all()
    lookup_url_kwarg = 'id'


class QuestionAndAnswersListByCourseView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = QuestionAndAnswersSerializer

    def get_queryset(self):
        questions = QuestionAndAnswer.objects.filter(course_id=self.kwargs['id'])
        return questions


class QuestionAndAnswersCreateView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = QuestionAndAnswersSerializer
    queryset = QuestionAndAnswer.objects.all()


class QuestionAndAnswersEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = QuestionAndAnswersSerializer
    queryset = QuestionAndAnswer.objects.all()
    lookup_url_kwarg = 'id'


class ResultListByCourseView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ResultSerializer

    def get_queryset(self):
        results = Result.objects.filter(course_id=self.kwargs['id'])
        return results


class ResultCreateView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ResultSerializer
    queryset = Result.objects.all()


class ResultEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
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
    permission_classes = [AllowAny]
    serializer_class = GallerySerializer
    queryset = Gallery.objects.all()

    def get(self, request, *args, **kwargs):
        serializer = GallerySerializer(Gallery.objects.get(menu_id=self.kwargs['id']))
        return Response(serializer.data)


class PostListByProgramView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Post.objects.filter(menu_id=self.kwargs['id'])
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)


class InformationContentByMenuView(APIView):
    permission_classes = [AllowAny]
    serializers = InformationContentSerializer

    def get(self, request, *args, **kwargs):
        queryset = InformationContent.objects.get(course_id=self.kwargs['id'])
        serializer = InformationContentSerializer(queryset)
        return Response(serializer.data)


class CourseInformationView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = CourseInformationSerializer
    lookup_url_kwarg = 'id'
    queryset = Course.objects.all()


class ProgramInformationView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProgramInformationSerializer
    queryset = Program.objects.all()
    lookup_url_kwarg = 'id'


class MenuBlogView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = MenuBlogSerializer
    queryset = Menu.objects.all()
    lookup_url_kwarg = 'id'


class CourseNameView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CourseNameSerializer
    queryset = Course.objects.all()


class LanguageView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()


class LanguageEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Language.objects.all()
    lookup_url_kwarg = 'id'


class LifeHackView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = LifeHackSerializer
    queryset = LifeHack.objects.filter(is_active=True)


class LifeHackEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = LifeHackSerializer
    queryset = LifeHack.objects.all()
    lookup_url_kwarg = 'id'


class MenuCoursesView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = MenuCoursesSerializer
    queryset = Menu.objects.all()
    lookup_url_kwarg = 'id'


class MainTitleView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = MainTitleSerializer
    queryset = MainTitle.objects.all()


class MainTitleEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = MainTitleSerializer
    queryset = MainTitle.objects.all()
    lookup_url_kwarg = 'id'

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from api.v1.admin.serializers import (
    PostSerializer,
    MenuSerializer,
    GallerySerializer,
    TeacherSerializer,
    AdvertisementSerializer,
    ProgramSerializer,
    FeedbackSerializer,
    GalleryFileSerializer,
    SubscriptionRequestSerializer,
    CompanySerializer,
    CourseSerializer,
    CourseFileSerializer,
    CourseInfoSerializer,
    CourseInfoDetailSerializer,
    CostOfEducationSerializer,
    CertificateSerializer,
    ProgramTrainingSerializer,
    ResultSerializer
)
from user.models import (
    Post,
    Menu,
    Gallery,
    Teacher,
    Advertisement,
    Program,
    Feedback,
    GalleryFile,
    SubscriptionRequest,
    CourseFile,
    Company,
    Course,
    CourseInfo,
    CourseInfoDetail,
    CostOfEducation,
    Certificate,
    ProgramTraining,
    Result
)


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
    queryset = Gallery.objects.all()


class GalleryEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = GallerySerializer
    permission_classes = [AllowAny, ]
    queryset = Gallery.objects.all()
    lookup_url_kwarg = 'id'


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


class ProgramCreateView(ListCreateAPIView):
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
    queryset = Advertisement.objects.all()


class AdvertisementEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = AdvertisementSerializer
    permission_classes = [AllowAny]
    queryset = Advertisement.objects.all()
    lookup_url_kwarg = 'id'


class FeedbackCreateView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()


class FeedbackEditView(RetrieveDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    lookup_url_kwarg = 'id'


class SubscriptionRequestCreateView(ListCreateAPIView):
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


class CourseInfoCreateView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CourseInfoSerializer
    queryset = CourseInfo.objects.all()


class CourseInfoEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = CourseInfoSerializer
    queryset = CourseInfo.objects.all()
    lookup_url_kwarg = 'id'


class CourseInfoDetailCreateView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CourseInfoDetailSerializer
    queryset = CourseInfoDetail.objects.all()


class CourseInfoDetailEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = CourseInfoDetailSerializer
    queryset = CourseInfoDetail.objects.all()
    lookup_url_kwarg = 'id'


class CostEducationCreateView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CostOfEducationSerializer
    queryset = CostOfEducation.objects.all()


class CostEducationEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = CostOfEducationSerializer
    queryset = CostOfEducation.objects.all()
    lookup_url_kwarg = 'id'


class CertificateCreateView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CertificateSerializer
    queryset = Certificate.objects.all()


class CertificateEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = CertificateSerializer
    queryset = Certificate.objects.all()
    lookup_url_kwarg = 'id'


class ProgramTrainingCreateView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProgramTrainingSerializer
    queryset = ProgramTraining.objects.all()


class ProgramTrainingEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProgramTrainingSerializer
    queryset = ProgramTraining.objects.all()
    lookup_url_kwarg = 'id'


class ResultCreateView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ResultSerializer
    queryset = Result.objects.all()


class ResultEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = ResultSerializer
    queryset = Result.objects.all()
    lookup_url_kwarg = 'id'

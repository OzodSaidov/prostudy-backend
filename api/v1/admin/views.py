from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView, \
    ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.admin.serializers import *
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
    queryset = Gallery.objects.all()


class GalleryEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = GallerySerializer
    permission_classes = [AllowAny, ]
    queryset = Gallery.objects.all()
    lookup_url_kwarg = 'id'


class TeacherListByCourseView(ListAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny, ]
    queryset = Teacher.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Teacher.objects.filter(course_id=self.kwargs['id'])
        serializer = TeacherSerializer(queryset, many=True)
        return Response(serializer.data)


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
    queryset = Program.objects.all()
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        queryset = Program.objects.filter(course_id=self.kwargs['id'])
        serializer = ProgramSerializer(queryset, many=True)
        return Response(serializer.data)


class InfoContentByProgramView(APIView):
    serializer_class = InformationContentSerializer
    queryset = InformationContent.objects.all()
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        try:
            queryset = InformationContent.objects.get(program_id=self.kwargs['id'])
            serializer = InformationContentSerializer(queryset)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(status=404)


class QuestionListByProgramView(APIView):
    serializer_class = QuestionAndAnswersSerializer
    queryset = QuestionAndAnswers.objects.all()
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        print(kwargs['id'])
        queryset = QuestionAndAnswers.objects.filter(program_id=self.kwargs['id'])
        serializer = QuestionAndAnswersSerializer(queryset, many=True)
        return Response(serializer.data)


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


class InformationContentByCourseView(APIView):
    permission_classes = [AllowAny]
    serializer_class = InformationContentSerializer
    queryset = InformationContent.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            queryset = InformationContent.objects.get(course_id=self.kwargs['id'])
            serializer = InformationContentSerializer(queryset)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(status=404)


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
    queryset = CostOfEducation.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = CostOfEducation.objects.filter(course_id=self.kwargs['id'])
        serializer = CostOfEducationSerializer(queryset, many=True)
        return Response(serializer.data)


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
        try:
            serializer = CertificateSerializer(Certificate.objects.get(course_id=self.kwargs['id']))
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(status=404)


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
    queryset = QuestionAndAnswers.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = QuestionAndAnswers.objects.filter(course_id=self.kwargs['id'])
        serializer = QuestionAndAnswersSerializer(queryset, many=True)
        return Response(serializer.data)


class QuestionAndAnswersCreateView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = QuestionAndAnswersSerializer
    queryset = QuestionAndAnswers.objects.all()


class QuestionAndAnswersEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = QuestionAndAnswersSerializer
    queryset = QuestionAndAnswers.objects.all()
    lookup_url_kwarg = 'id'


class ResultListByCourseView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ResultSerializer
    queryset = Result.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Result.objects.filter(course_id=self.kwargs['id'])
        serializer = ResultSerializer(queryset, many=True)
        return Response(serializer.data)


class ResultCreateView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ResultSerializer
    queryset = Result.objects.all()


class ResultEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = ResultSerializer
    queryset = Result.objects.all()
    lookup_url_kwarg = 'id'

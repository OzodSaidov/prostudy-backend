from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest
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

    def get(self, request, *args, **kwargs):
        course = Course.objects.get(programs=self.kwargs['id'])
        gallery = Gallery.objects.get(course_id=course.id)
        serializer = GallerySerializer(gallery)
        return Response(serializer.data)


class TeacherListByCourseView(ListAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny, ]
    queryset = Teacher.objects.all()

    def get(self, request, *args, **kwargs):
        # domain = request.scheme + '://' + request.get_host()
        queryset = Teacher.objects.filter(course_id=self.kwargs['id'])
        serializer = TeacherSerializer(queryset, many=True)
        # list_teachers = []
        # for data in serializer.data:
        #     context = {
        #         "first_name": data['first_name'],
        #         "last_name": data['last_name'],
        #         "photo": domain + data['photo'],
        #         "specialty": data['specialty'],
        #         "experience": data['experience'],
        #     }
        #     list_teachers.append(context)
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
        # domain = request.scheme + '://' + request.get_host()
        queryset = Program.objects.filter(course_id=self.kwargs['id'])
        serializer = ProgramSerializer(queryset, many=True)
        # list_programs = []
        # for data in serializer.data:
        #     context = {
        #         "id": data['id'],
        #         "title": data['title'],
        #         "image": domain + data['image'],
        #     }
        #     list_programs.append(context)
        return Response(serializer.data)


class InfoContentByProgramView(APIView):
    serializer_class = InformationContentSerializer
    queryset = InformationContent.objects.all()
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        queryset = InformationContent.objects.get(program_id=self.kwargs['id'])
        serializer = InformationContentSerializer(queryset)
        return Response(serializer.data)


class QuestionListByProgramView(APIView):
    serializer_class = QuestionAndAnswersSerializer
    queryset = QuestionAndAnswer.objects.all()
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        queryset = QuestionAndAnswer.objects.filter(program_id=self.kwargs['id'])
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
    queryset = InformationContent.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = InformationContent.objects.get(course_id=self.kwargs['id'])
        serializer = InformationContentSerializer(queryset)
        # domain = request.scheme + '://' + request.get_host()
        # title = serializer.data['title']
        # body = serializer.data['body']
        # background = serializer.data['background']
        # if background:
        #     background = domain + background
        # list_content_detail = serializer.data['information_content_detail']
        # inf_content_detail = []
        # for content in list_content_detail:
        #     detail = {
        #         "title": content['title'],
        #         "body": content['body'],
        #         "image": domain + content['image']
        #     }
        #     inf_content_detail.append(detail)
        # context = {
        #     "title": title,
        #     "body": body,
        #     "background": background,
        #     "information_content_detail": inf_content_detail
        # }
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
    queryset = CostOfEducation.objects.all()

    def get(self, request, *args, **kwargs):
        # domain = request.scheme + '://' + request.get_host()
        queryset = CostOfEducation.objects.filter(course_id=self.kwargs['id'])
        serializer = CostOfEducationSerializer(queryset, many=True)
        # list_cost_education = []
        # for data in serializer.data:
        #     context = {
        #         "title": data['title'],
        #         "body": data['body'],
        #         "old_price": data['old_price'],
        #         "new_price": data['new_price'],
        #         "image": domain + data['image'],
        #     }
        #     list_cost_education.append(context)
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
        cert = Certificate.objects.get(course_id=self.kwargs['id'])
        serializer = CertificateSerializer(cert)
        # title = serializer.data['title']
        # image = serializer.data['image']
        # domain = request.scheme + '://' + request.get_host()
        # image_url = domain + image
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
    queryset = QuestionAndAnswer.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = QuestionAndAnswer.objects.filter(course_id=self.kwargs['id'])
        serializer = QuestionAndAnswersSerializer(queryset, many=True)
        return Response(serializer.data)


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


class PostByMenuView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        # domain = request.scheme + '://' + request.get_host()
        posts = Post.objects.filter(menu_id=self.kwargs['id'])
        serializer = PostSerializer(posts, many=True)
        # post_list = []
        # for post in serializer.data:
        #     post_data = {
        #         "title": post['title'],
        #         "content": post['content'],
        #         "short_content": post['short_content'],
        #
        #         "post_images": post['post_images']['file']
        #     }
        #     post_list.append(post_data)
        #     print(post_list)
        return Response(serializer.data)


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

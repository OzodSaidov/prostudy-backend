from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser

from api.v1.admin.serializers import *
from user.models import *


class PostCreateView(ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)
    queryset = Post.objects.all()


class PostEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)
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


class GalleryCreateView(ListCreateAPIView):
    serializer_class = GallerySerializer
    permission_classes = [AllowAny, ]
    queryset = Gallery.objects.all()


class GalleryEditView(RetrieveDestroyAPIView):
    serializer_class = GallerySerializer
    permission_classes = [AllowAny, ]
    queryset = Gallery.objects.all()
    lookup_url_kwarg = 'id'


class TeacherCreateView(ListCreateAPIView):
    parser_classes = [MultiPartParser]
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny, ]
    queryset = Teacher.objects.all()


class TeacherEditView(RetrieveUpdateDestroyAPIView):
    parser_classes = [MultiPartParser]
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny, ]
    queryset = Teacher.objects.all()
    lookup_url_kwarg = 'id'


class CourseCreateView(ListCreateAPIView):
    parser_classes = [MultiPartParser]
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]
    queryset = Course.objects.all()


class CourseEditView(RetrieveUpdateDestroyAPIView):
    parser_classes = [MultiPartParser]
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]
    queryset = Course.objects.all()
    lookup_url_kwarg = 'id'


class AdvertisementCreateView(ListCreateAPIView):
    parser_classes = [MultiPartParser]
    serializer_class = AdvertisementSerializer
    permission_classes = [AllowAny]
    queryset = Advertisement.objects.all()


class AdvertisementEditView(RetrieveUpdateDestroyAPIView):
    parser_classes = [MultiPartParser]
    serializer_class = AdvertisementSerializer
    permission_classes = [AllowAny]
    queryset = Advertisement.objects.all()
    lookup_url_kwarg = 'id'


class ReviewCreateView(ListCreateAPIView):
    pass


class ReviewEditView(RetrieveUpdateDestroyAPIView):
    pass


class FeedbackCreateView(ListCreateAPIView):
    pass


class FeedbackEditView(RetrieveUpdateDestroyAPIView):
    pass


class SubscriptionRequestCreateView(ListCreateAPIView):
    pass


class SubscriptionRequestEditView(RetrieveUpdateDestroyAPIView):
    pass


class ProgramCreateView(ListCreateAPIView):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()
    permission_classes = [AllowAny]

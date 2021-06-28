from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from api.v1.admin.serializers import PostSerializer, MenuSerializer, GallerySerializer, \
    TeacherSerializer, CourseSerializer, AdvertisementSerializer, ProgramSerializer, FeedbackSerializer, \
    GalleryFileSerializer, SubscriptionRequestSerializer
from user.models import Post, Menu, Gallery, Teacher, Course, Advertisement, Program, Feedback, GalleryFile, \
    SubscriptionRequest


class PostCreateView(ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()


class PostEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    lookup_url_kwarg = 'id'


class MenuCreateView(ListCreateAPIView):
    serializer_class = MenuSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Menu.objects.filter(parent=None)


class MenuEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = MenuSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Menu.objects.all()
    lookup_url_kwarg = 'id'


class GalleryFileCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = GalleryFileSerializer
    queryset = GalleryFile.objects.all()


class GalleryFileRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = GalleryFile.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = GalleryFileSerializer
    lookup_url_kwarg = 'id'


class GalleryCreateView(ListCreateAPIView):
    serializer_class = GallerySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Gallery.objects.all()


class GalleryEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = GallerySerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Gallery.objects.all()
    lookup_url_kwarg = 'id'


class TeacherCreateView(ListCreateAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Teacher.objects.all()


class TeacherEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Teacher.objects.all()
    lookup_url_kwarg = 'id'


class CourseCreateView(ListCreateAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Course.objects.all()


class CourseEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()
    lookup_url_kwarg = 'id'


class ProgramCreateView(ListCreateAPIView):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProgramEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()
    lookup_url_kwarg = 'id'


class AdvertisementCreateView(ListCreateAPIView):
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Advertisement.objects.all()


class AdvertisementEditView(RetrieveUpdateDestroyAPIView):
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated]
    queryset = Advertisement.objects.all()
    lookup_url_kwarg = 'id'


class FeedbackCreateView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()


class FeedbackEditView(RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    lookup_url_kwarg = 'id'


class SubscriptionRequestCreateView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = SubscriptionRequestSerializer
    queryset = SubscriptionRequest


class SubscriptionRequestEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SubscriptionRequestSerializer
    queryset = SubscriptionRequest
    lookup_url_kwarg = 'id'

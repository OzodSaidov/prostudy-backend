from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import AllowAny

from api.v1.admin.serializers import PostSerializer, MenuSerializer, GallerySerializer
from user.models import Post, Menu, Gallery


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

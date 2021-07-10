from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from api.v1.region.serializers import RegionsSerializer
from region.models import Region


class RegionsView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegionsSerializer
    queryset = Region.objects.all()
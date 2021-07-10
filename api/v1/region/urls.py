from django.urls import path

from api.v1.region.views import RegionsView

urlpatterns = [
    path('', RegionsView.as_view())
]
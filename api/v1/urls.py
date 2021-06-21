from django.urls import path, include

app_name = 'api_v1'
urlpatterns = [
    path('admin/', include('api.v1.admin.urls'))
]

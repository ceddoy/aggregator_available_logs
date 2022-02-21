from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from agregatorapp.views import LogListAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
    path('api/logs/', LogListAPIView.as_view()),
    path('silk/', include('silk.urls', namespace='silk')),

]

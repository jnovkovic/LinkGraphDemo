from django.conf.urls import url
from rest_framework.authtoken import views

from .views import UserRegisterAPIView


urlpatterns = [
    url(r'^create/$', UserRegisterAPIView.as_view()),
    url(r'^login/$', views.ObtainAuthToken.as_view()),
]

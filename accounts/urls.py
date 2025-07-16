from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

from . import views

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", ObtainAuthToken.as_view(), name="login"),
]
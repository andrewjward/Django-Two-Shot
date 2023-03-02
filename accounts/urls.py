from django.urls import path
from accounts.views import Login

urlpatterns = [path("login/", Login, name="login")]

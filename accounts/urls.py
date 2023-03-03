from django.urls import path
from accounts.views import Login, Logout, Signup

urlpatterns = [
    path("login/", Login, name="login"),
    path("logout/", Logout, name="logout"),
    path("signup/", Signup, name="signup"),
]

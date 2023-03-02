from django.urls import path
from accounts.views import Login, Logout

urlpatterns = [
    path("login/", Login, name="login"),
    path("logout/", Logout, name="logout"),
]

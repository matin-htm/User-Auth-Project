from django.urls import path
from .views import HomePageView, UsersPageView, SignUpView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("users/", UsersPageView.as_view(), name="users"),
    path("users/signup/", SignUpView.as_view(), name="signup"),
]

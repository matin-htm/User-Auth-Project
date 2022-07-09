from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    template_name = "home.html"


class UsersPageView(TemplateView):
    template_name = "users.html"


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("users")
    template_name = "signup.html"

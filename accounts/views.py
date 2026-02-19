from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm
from .mixins import RedirectAuthenticatedUserMixin


class SignUpView(RedirectAuthenticatedUserMixin, CreateView):
    form_class = SignUpForm
    template_name = "auth/signup.html"
    success_url = reverse_lazy("login")

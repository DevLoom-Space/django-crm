from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from crm.forms import BootstrapFormMixin


class SignUpForm(BootstrapFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_bootstrap()

from apps.user.models import *
from django_registration.forms import RegistrationFormCaseInsensitive


class MyCustomUserForm(RegistrationFormCaseInsensitive):
    class Meta(RegistrationFormCaseInsensitive.Meta):
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'university_id', 'email', 'password1', 'password2')
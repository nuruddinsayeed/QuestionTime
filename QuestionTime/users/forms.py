from django_registration.forms import RegistrationForm
from users.models import CustomUSer


class CustomUserForm(RegistrationForm):
    """Regirtration from to create new user"""

    class Meta(RegistrationForm.Meta):
        model = CustomUSer

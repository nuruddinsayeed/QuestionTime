
from django.contrib import admin
from django.urls import path, re_path
from django.urls.conf import include

from django_registration.backends.one_step.views import RegistrationView

from core.views import IndexTemplateview
from users.forms import CustomUserForm

urlpatterns = [
    path('admin/', admin.site.urls),

    path("account/register/",
         RegistrationView.as_view(
             form_class=CustomUserForm,
             success_url="/"
         ), name="django_registration_register"),
    path("account/", include("django_registration.backends.one_step.urls")),
    path("account/", include("django.contrib.auth.urls")),

    path("api/", include("users.api.urls")),

    path("api-auth/", include("rest_framework.urls")),
    path("api/rest-auth/", include("rest_auth.urls")),
    path("api/rest-auth/registration/", include("rest_auth.registration.urls")),

    re_path(r"^.*$", IndexTemplateview.as_view(), name="entry-point")
]

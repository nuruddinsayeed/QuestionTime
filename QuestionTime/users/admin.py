from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUSer


class CustomUserAdmin(UserAdmin):
    model = CustomUSer
    list_display = ["username", "email", "is_staff"]


admin.site.register(CustomUSer, CustomUserAdmin)

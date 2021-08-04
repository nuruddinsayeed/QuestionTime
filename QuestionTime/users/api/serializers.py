from rest_framework import serializers
from users.models import CustomUSer


class UserDisplaySerializer(serializers.ModelSerializer):
    """Serializes user model"""

    class Meta:
        model = CustomUSer
        fields = ["username"]

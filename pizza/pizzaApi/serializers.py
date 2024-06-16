from rest_framework.serializers import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["firstName", "lastName", "phoneNumber", "email"]
    
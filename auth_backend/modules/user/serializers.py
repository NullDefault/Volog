from rest_framework import serializers

from auth_backend.modules.user.models import BaseVologUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseVologUser
        fields = '__all__'

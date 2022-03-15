from rest_framework import serializers
from .models import User


class AllUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'message']

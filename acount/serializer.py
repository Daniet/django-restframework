from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
        validate_password = make_password
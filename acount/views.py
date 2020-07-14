from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from . import serializer

# Create your views here.
class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = serializer.UserSerializer

    def create(self, request, *args, **kwargs):
        user = User()
        user.username = request.data['username']
        user.first_name = request.data['first_name']
        user.last_name = request.data['last_name']
        user.email = request.data['email']
        user.set_password(request.data['password'])
        user.save()
        return Response({
            'username': user.username
        }, status=status.HTTP_201_CREATED)

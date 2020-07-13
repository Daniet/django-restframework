from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.
class MethodHttp(viewsets.ViewSet):

    def list(self, request, *args, **kwargs):
        return Response({
            'Http': 'GET',
            'params': kwargs,
        }, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        return Response({
            'Http': 'GET',
            'params': kwargs,
        }, status=status.HTTP_201_CREATED)

    def create(self, request, *args, **kwargs):
        return Response({
            'Http': 'POST',
            'params': kwargs,
            'data': request.data,
        }, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        return Response({
            'Http': 'PUT',
            'params': kwargs,
            'data': request.data,
        }, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        return Response({
            'Http': 'PATCH',
            'params': kwargs,
            'data': request.data,
        }, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        return Response({
            'Http': 'DELETE',
            'params': kwargs,
        }, status=status.HTTP_200_OK)
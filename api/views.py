from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from api.models import User
from api.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from api.models import User


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

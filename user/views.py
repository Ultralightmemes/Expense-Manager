from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny

from user.models import User
from user.serializers import RegistrationSerializer


class RegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

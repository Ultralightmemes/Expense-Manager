from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from user.models import User
from user.serializers import RegistrationSerializer, UserSerializer


class RegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer


class UserAPIView(generics.RetrieveUpdateAPIView):

    def get(self, request):
        user = User.objects.get(email=request.user.email)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def patch(self, request):
        user = User.objects.get(email=request.user.email)
        serializer = UserSerializer(user, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

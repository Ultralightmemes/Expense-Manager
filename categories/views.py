from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.db import transaction

from categories.models import Category
from categories.serializers import CategorySerializer
from user.models import UserCategory


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(users__email=self.request.user.email, usercategory__is_active=True)

    def create(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            with transaction.atomic():
                category = serializer.save()
                UserCategory.objects.create(user=request.user, category=category)
            return Response(data=serializer.validated_data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.default:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                user_category = UserCategory.objects.get(category=instance, user__email=request.user.email)
                user_category.is_active = False
                with transaction.atomic():
                    user_category.save()
                    category = serializer.save()
                    UserCategory.objects.create(user=request.user, category=category)
        else:
            serializer = CategorySerializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
        return Response(data=serializer.validated_data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user_category = UserCategory.objects.get(category=instance, user__email=request.user.email)
        user_category.is_active = False
        user_category.save()
        serializer = CategorySerializer(instance)
        return Response(data=serializer.data)

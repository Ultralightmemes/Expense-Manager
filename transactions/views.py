import django_filters
from rest_framework import viewsets, permissions, status, filters
from django.db import transaction as trn
from rest_framework.response import Response

from categories.models import Category
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer
from user.models import User


class IsAuthorOrIsAuthenticated(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class TransactionsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrIsAuthenticated, )
    serializer_class = TransactionSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['date_done', 'sum']
    ordering_fields = ['date_done', 'sum']

    def get_queryset(self):
        return Transaction.objects.filter(user__email=self.request.user.email)

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            with trn.atomic():
                transaction = serializer.save(user=request.user)
                user = User.objects.get(email=request.user.email)
                user.balance += transaction.sum
                user.save()
            return Response(data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)





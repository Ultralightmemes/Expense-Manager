from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from categories.models import Category
from categories.serializers import CategorySerializer
from transactions.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        exclude = ('user',)




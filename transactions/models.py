from django.db import models

from categories.models import Category
from user.models import User


class Transaction(models.Model):
    sum = models.FloatField(verbose_name='Сумма')
    date_done = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, verbose_name='Категория', null=True, on_delete=models.SET_NULL)
    organization = models.CharField(max_length=255, verbose_name='Организация')
    description = models.CharField(max_length=255, blank=True, verbose_name='Описание')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'

    def __str__(self):
        return self.description




from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Название')
    default = models.BooleanField(default=False, verbose_name='Стандартная')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name


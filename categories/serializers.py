from rest_framework import serializers

from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'category_name', ]


# class CategoryUpdateSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField()
#
#     class Meta:
#         model = Category
#         fields = ['id', 'category_name', ]
#
#     def update(self, instance, validated_data):
#         if instance.default:
#             instance.id = None
#         instance.category_name = validated_data.get('category_name', instance.category_name)
#         instance.save()
#         return instance



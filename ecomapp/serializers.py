from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'parent')
        model = Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'price', 'category')
        model = Product

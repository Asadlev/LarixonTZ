from rest_framework import serializers
from .models import Advert, Category, City


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name'
        ]


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = [
            'name'
        ]


class AdvertSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    category = CategorySerializer()

    class Meta:
        model = Advert
        fields = [
            'created',
            'title',
            'description',
            'city',
            'category',
            'views'
        ]

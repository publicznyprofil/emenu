from rest_framework import serializers

from .models import (
    Menu,
    Dish,
)


class MenuListSerializer(serializers.ModelSerializer):
    dish_number = serializers.IntegerField()

    class Meta:
        model = Menu
        fields = ('id', 'name', 'dish_number', 'description')


class DistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('name', 'description', 'price', 'preparation_time', 'is_vegetarian')

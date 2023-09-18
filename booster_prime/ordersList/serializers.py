from rest_framework import serializers
from .models import Fuel, Order


class FuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = '__all__'


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
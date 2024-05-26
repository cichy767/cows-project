from rest_framework import serializers
from .models import Cow, Weight, Feeding, MilkProduction


class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = '__all__'


class FeedingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeding
        fields = '__all__'


class MilkProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilkProduction
        fields = '__all__'


class CowSerializer(serializers.ModelSerializer):
    weight = WeightSerializer()
    feeding = FeedingSerializer()
    milk_production = MilkProductionSerializer()

    class Meta:
        model = Cow
        fields = '__all__'

from collections.abc import Mapping
from datetime import datetime
from typing import Any
from uuid import UUID

from django.db import transaction
from pydantic import BaseModel, Field, ValidationError
from rest_framework import serializers

from .models import Cow, Weight, Feeding, MilkProduction


class WeightModel(BaseModel):
    mass_kg: float
    last_measured: datetime


class FeedingModel(BaseModel):
    amount_kg: float
    cron_schedule: str
    last_measured: datetime


class MilkProductionModel(BaseModel):
    last_milk: datetime
    cron_schedule: str
    amount_l: float


class CowModel(BaseModel):
    id: UUID = Field(None, alias='id')
    name: str
    sex: str
    birthdate: datetime
    condition: str

    has_calves: bool
    weight: WeightModel
    feeding: FeedingModel
    milk_production: MilkProductionModel


class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = ['mass_kg', 'last_measured']


class FeedingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeding
        fields = ['amount_kg', 'cron_schedule', 'last_measured']


class MilkProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilkProduction
        fields = ['last_milk', 'cron_schedule', 'amount_l']


class CowSerializer(serializers.ModelSerializer):
    weight = WeightSerializer()
    feeding = FeedingSerializer()
    milk_production = MilkProductionSerializer()

    class Meta:
        model = Cow
        fields = ['id', 'name', 'sex', 'birthdate', 'condition', 'weight',
                  'feeding', 'milk_production', 'has_calves']

    def validate(self, data: Mapping[str, Any]) -> dict[str, Any]:
        try:
            CowModel(**data)
        except ValidationError as e:
            raise serializers.ValidationError(e.errors())
        return data

    @transaction.atomic
    def create(self, validated_data: dict[str, Any]) -> Cow:
        weight_data = validated_data.pop('weight')
        feeding_data = validated_data.pop('feeding')
        milk_production_data = validated_data.pop('milk_production')

        weight = Weight.objects.create(**weight_data)
        feeding = Feeding.objects.create(**feeding_data)
        milk_production = MilkProduction.objects.create(**milk_production_data)

        cow = Cow.objects.create(
            weight=weight,
            feeding=feeding,
            milk_production=milk_production,
            **validated_data
        )
        return cow

    @transaction.atomic
    def update(self, instance: Cow, validated_data: dict[str, Any]) -> Cow:
        weight_data = validated_data.pop('weight')
        feeding_data = validated_data.pop('feeding')
        milk_production_data = validated_data.pop('milk_production')

        weight = instance.weight
        feeding = instance.feeding
        milk_production = instance.milk_production

        instance.name = validated_data.get('name', instance.name)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.birthdate = validated_data.get(
            'birthdate',
            instance.birthdate
        )
        instance.condition = validated_data.get(
            'condition',
            instance.condition
        )
        instance.has_calves = validated_data.get(
            'has_calves',
            instance.has_calves
        )
        instance.save()

        weight.mass_kg = weight_data.get('mass_kg', weight.mass_kg)
        weight.last_measured = weight_data.get(
            'last_measured',
            weight.last_measured
        )
        weight.save()

        feeding.amount_kg = feeding_data.get('amount_kg', feeding.amount_kg)
        feeding.cron_schedule = feeding_data.get(
            'cron_schedule',
            feeding.cron_schedule
        )
        feeding.last_measured = feeding_data.get(
            'last_measured',
            feeding.last_measured
        )
        feeding.save()

        milk_production.last_milk = milk_production_data.get(
            'last_milk',
            milk_production.last_milk
        )
        milk_production.cron_schedule = milk_production_data.get(
            'cron_schedule', milk_production.cron_schedule
        )
        milk_production.amount_l = milk_production_data.get(
            'amount_l',
            milk_production.amount_l
        )
        milk_production.save()

        return instance

from django.db import models


class Weight(models.Model):
    mass_kg = models.IntegerField()
    last_measured = models.DateTimeField()


class Feeding(models.Model):
    amount_kg = models.IntegerField()
    cron_schedule = models.CharField(max_length=100)
    last_measured = models.DateTimeField()


class MilkProduction(models.Model):
    last_milk = models.DateTimeField()
    cron_schedule = models.CharField(max_length=100)
    amount_l = models.IntegerField()


class Cow(models.Model):
    last_updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    birthdate = models.DateTimeField()
    condition = models.CharField(max_length=100)
    weight = models.OneToOneField(Weight, on_delete=models.CASCADE)
    feeding = models.OneToOneField(Feeding, on_delete=models.CASCADE)
    milk_production = models.OneToOneField(MilkProduction, on_delete=models.CASCADE)
    has_calves = models.BooleanField()

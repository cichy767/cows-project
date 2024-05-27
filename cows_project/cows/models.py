from django.db import models
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Weight(BaseModel):
    mass_kg = models.IntegerField()
    last_measured = models.DateTimeField()


class Feeding(BaseModel):
    amount_kg = models.IntegerField()
    cron_schedule = models.CharField(max_length=100)
    last_measured = models.DateTimeField()


class MilkProduction(BaseModel):
    last_milk = models.DateTimeField()
    cron_schedule = models.CharField(max_length=100)
    amount_l = models.IntegerField()


class Cow(BaseModel):
    MALE = 'male'
    FEMALE = 'female'
    SEX_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    birthdate = models.DateTimeField()
    condition = models.CharField(max_length=100)
    weight = models.OneToOneField(Weight, on_delete=models.CASCADE)
    feeding = models.OneToOneField(Feeding, on_delete=models.CASCADE)
    milk_production = models.OneToOneField(MilkProduction, on_delete=models.CASCADE)
    has_calves = models.BooleanField()

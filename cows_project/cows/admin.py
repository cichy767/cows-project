from django.contrib import admin
from .models import Cow, Weight, Feeding, MilkProduction


@admin.register(Cow)
class CowAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'birthdate', 'condition', 'has_calves')
    search_fields = ('name', 'sex', 'condition')


@admin.register(Weight)
class WeightAdmin(admin.ModelAdmin):
    list_display = ('id', 'mass_kg', 'last_measured')


@admin.register(Feeding)
class FeedingAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount_kg', 'cron_schedule', 'last_measured')


@admin.register(MilkProduction)
class MilkProductionAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_milk', 'cron_schedule', 'amount_l')

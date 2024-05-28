import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Cow, Weight, Feeding, MilkProduction


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_cow():
    weight = Weight.objects.create(
        mass_kg=500, last_measured='2023-01-01T00:00:00Z'
    )
    feeding = Feeding.objects.create(
        amount_kg=30, cron_schedule="0 */6 * * *",
        last_measured='2023-01-01T00:00:00Z'
    )
    milk_production = MilkProduction.objects.create(
        last_milk='2023-01-01T00:00:00Z',
        cron_schedule="0 8,12,16,20 * * *",
        amount_l=20
    )
    cow = Cow.objects.create(
        name='Bessie', sex='Female', birthdate='2019-02-11T03:21:00Z',
        condition='Healthy',
        weight=weight, feeding=feeding, milk_production=milk_production,
        has_calves=True
    )
    return cow


@pytest.mark.django_db
def test_create_cow(api_client):
    url = reverse('cow-list')
    data = {
        "name": "Betty",
        "sex": "male",
        "birthdate": "2019-02-11T03:21:00.000000Z",
        "condition": "Healthy",
        "weight": {
            "mass_kg": 1100,
            "last_measured": "2022-11-02T11:15:00.000000Z"
        },
        "feeding": {
            "amount_kg": 5,
            "cron_schedule": "0 */6 * * *",
            "last_measured": "2022-11-02T11:00:00.000000Z"
        },
        "milk_production": {
            "last_milk": "2022-11-02T09:00:00.000000Z",
            "cron_schedule": "0 8,12,16,20 * * *",
            "amount_l": 5
        },
        "has_calves": True
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Cow.objects.count() == 1
    assert Cow.objects.get().name == 'Betty'


@pytest.mark.django_db
def test_get_cows(api_client, create_cow):
    url = reverse('cow-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()[0]['name'] == create_cow.name


@pytest.mark.django_db
def test_update_cow(api_client, create_cow):
    url = reverse('cow-detail',
                  kwargs={'id': create_cow.id})  # Use 'id' as the lookup field
    data = {
        "name": "Bessie Updated",
        "sex": "female",
        "birthdate": "2019-02-11T03:21:00Z",
        "condition": "Healthy",
        "weight": {
            "mass_kg": 550,
            "last_measured": "2023-01-01T00:00:00Z"
        },
        "feeding": {
            "amount_kg": 35,
            "cron_schedule": "0 */6 * * *",
            "last_measured": "2023-01-01T00:00:00Z"
        },
        "milk_production": {
            "last_milk": "2023-01-01T00:00:00Z",
            "cron_schedule": "0 8,12,16,20 * * *",
            "amount_l": 25
        },
        "has_calves": True
    }
    response = api_client.put(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK, response.content
    assert Cow.objects.get().name == 'Bessie Updated'


@pytest.mark.django_db
def test_delete_cow(api_client, create_cow):
    url = reverse('cow-detail',
                  kwargs={'id': create_cow.id})  # Use 'id' as the lookup field
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Cow.objects.count() == 0

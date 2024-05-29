from rest_framework import viewsets
from .models import Cow
from .serializers import CowSerializer


class CowViewSet(viewsets.ModelViewSet):
    queryset = Cow.objects.all()
    serializer_class = CowSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Cow.objects.select_related('weight', 'feeding', 'milk_production').all()

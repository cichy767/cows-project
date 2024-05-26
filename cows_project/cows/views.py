from rest_framework import viewsets
from .models import Cow
from .serializers import CowSerializer


class CowViewSet(viewsets.ModelViewSet):
    queryset = Cow.objects.all()
    serializer_class = CowSerializer

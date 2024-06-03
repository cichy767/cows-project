from rest_framework import viewsets
from .models import Cow
from .serializers import CowSerializer
from rest_framework.filters import SearchFilter


class CowViewSet(viewsets.ModelViewSet):
    queryset = Cow.objects.all()
    serializer_class = CowSerializer
    lookup_field = 'id'
    filter_backends = [SearchFilter]
    search_fields = ['sex']

    def get_queryset(self):
        queryset = Cow.objects.select_related(
            'weight', 'feeding', 'milk_production'
        )
        sex = self.request.query_params.get('sex')
        if sex:
            queryset = queryset.filter(sex=sex)
        return queryset

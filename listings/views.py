from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Car
from .serializers import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['brand', 'model_year', 'is_available']
    search_fields = ['name', 'brand']
    ordering_fields = ['price', 'model_year']

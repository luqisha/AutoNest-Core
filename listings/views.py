from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Car
from .models import Favorite
from .serializers import CarSerializer, FavoriteSerializer
from django.core.cache import cache
from rest_framework.response import Response
import redis


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['brand', 'model_year', 'is_available']
    search_fields = ['name', 'brand']
    ordering_fields = ['price', 'model_year']

    def retrieve(self, request, *args, **kwargs):
        car_id = kwargs['pk']

        # Redis connection
        r = redis.StrictRedis(host='localhost', port=6379, db=1)

        # Increment view count
        r.zincrby('car_views', 1, car_id)

        # Try to get car data from cache
        cache_key = f'car_detail_{car_id}'
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)

        # Cache miss: get from DB, cache it for 5 mins, then return
        car = self.get_object()
        serializer = self.get_serializer(car)
        cache.set(cache_key, serializer.data, timeout=300)

        return Response(serializer.data)


class FavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

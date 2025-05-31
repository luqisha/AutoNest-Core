from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, FavoriteViewSet


router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='car')
router.register(r'favorites', FavoriteViewSet, basename='favorite')

urlpatterns = [
    path('', include(router.urls)),
]

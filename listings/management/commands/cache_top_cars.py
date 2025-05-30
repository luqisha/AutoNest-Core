from django.core.cache import cache
from django.core.management.base import BaseCommand
from listings.utils.redis_helpers import get_top_5_car_ids

from listings.models import Car
from listings.serializers import CarSerializer


class Command(BaseCommand):
    help = 'Cache top 5 most viewed car details in Redis'

    def handle(self, *args, **kwargs):
        top_ids = get_top_5_car_ids()
        for car_id in top_ids:
            cache_key = f'car_detail_{car_id}'
            if not cache.get(cache_key):
                try:
                    car = Car.objects.get(id=car_id)
                    data = CarSerializer(car).data
                    cache.set(cache_key, data, timeout=300)
                    self.stdout.write(
                        self.style.SUCCESS(f"Cached car {car_id}"))
                except Car.DoesNotExist:
                    continue

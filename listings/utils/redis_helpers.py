import redis


def get_top_5_car_ids():
    r = redis.StrictRedis(host='localhost', port=6379, db=1)
    car_ids = r.zrevrange('car_views', 0, 4)
    return [int(car_id.decode()) for car_id in car_ids]

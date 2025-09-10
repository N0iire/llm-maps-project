# maps_api/middleware.py

import redis
from django.conf import settings
from django.http import JsonResponse
import time

redis_instance = redis.StrictRedis(host='redis', port=6379, db=0, decode_responses=True)

class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.limit = 20
        self.period = 3600

    def __call__(self, request):
        if not request.path.startswith('/api/find-place/'):
            return self.get_response(request)
        
        ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR'))
        if not ip:
            return self.get_response(request)

        key = f"rate-limit:{ip}"
        request_count = redis_instance.get(key)

        if request_count is not None and int(request_count) >= self.limit:
            return JsonResponse(
                {'error': 'Anda telah melampaui batas permintaan. Silakan coba lagi nanti.'},
                status=429
            )

        with redis_instance.pipeline() as pipe:
            pipe.incr(key, 1)
            if request_count is None:
                pipe.expire(key, self.period)
            pipe.execute()

        response = self.get_response(request)
        return response
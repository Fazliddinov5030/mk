# Ushbu sozlamalarni book/settings.py faylingizga qo'shing.
# `pip install django-redis` qilingan bo'lishi kerak.

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # Agar Redis server uzilib qolsa sayt "500 Error" bermasdan sekinroq ishlayverishi (Fallback) uchun:
            "IGNORE_EXCEPTIONS": True, 
        }
    }
}
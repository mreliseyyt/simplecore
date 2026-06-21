import time
import hashlib
from functools import wraps
from typing import Any, Callable

from .cache import Cache


def timer(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"⏱ {func.__name__} выполнен за {elapsed:.4f} сек")
        return result

    return wrapper


def retry(max_attempts: int = 3, delay: int = 1, exceptions: tuple = (Exception,)):

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"🔄 Попытка {attempt + 1} не удалась: {e}")
                    time.sleep(delay)
            return None

        return wrapper

    return decorator


def cached(ttl: int = 60):
    cache = Cache(ttl)

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Генерация ключа
            key_parts = [func.__name__]
            if args:
                key_parts.append(str(args))
            if kwargs:
                key_parts.append(str(sorted(kwargs.items())))
            key = hashlib.md5(''.join(key_parts).encode()).hexdigest()

            cached_value = cache.get(key)
            if cached_value is not None:
                print(f"💾 Кэш-хит для {func.__name__}")
                return cached_value

            result = func(*args, **kwargs)
            cache.set(key, result, ttl)
            return result

        return wrapper

    return decorator


def log_call(logger=None):

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            log = logger or print
            log(f"📞 Вызов {func.__name__} с аргументами: {args}, {kwargs}")
            result = func(*args, **kwargs)
            log(f"✅ {func.__name__} вернул: {result}")
            return result

        return wrapper

    return decorator
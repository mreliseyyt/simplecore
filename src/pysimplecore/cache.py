
import time
from typing import Any, Dict, Optional


class Cache:

    def __init__(self, default_ttl: int = 60):
        self._store: Dict[str, Dict[str, Any]] = {}
        self.default_ttl = default_ttl

    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        ttl = ttl or self.default_ttl
        self._store[key] = {
            'value': value,
            'expires': time.time() + ttl
        }

    def get(self, key: str) -> Optional[Any]:
        if key not in self._store:
            return None

        item = self._store[key]
        if time.time() > item['expires']:
            del self._store[key]
            return None

        return item['value']

    def delete(self, key: str) -> bool:
        if key in self._store:
            del self._store[key]
            return True
        return False

    def clear(self) -> None:
        self._store.clear()

    def has(self, key: str) -> bool:
        return self.get(key) is not None
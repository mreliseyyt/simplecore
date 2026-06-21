"""
Базовые тесты для pysimplecore
"""

import pytest
from pysimplecore import cache, serializer, validator

def test_cache():
    """Проверяем работу кэша"""
    c = cache.Cache(default_ttl=5)
    c.set("test_key", "test_value")
    assert c.get("test_key") == "test_value"

def test_serializer():
    """Проверяем сериализацию"""
    data = {"name": "test", "value": 123}
    json_str = serializer.Serializer.to_json(data)
    assert "test" in json_str
    assert "123" in json_str

def test_validator_email():
    """Проверяем валидацию email"""
    assert validator.Validator.is_email("test@example.com") is True
    assert validator.Validator.is_email("invalid-email") is False
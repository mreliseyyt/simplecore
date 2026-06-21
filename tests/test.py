

import time
import pysimplecore


def main():
    """Тест кэширования"""
    print("\n" + "=" * 50)
    print("🧪 ТЕСТ 1: Кэширование")
    print("=" * 50)

    cache = Cache(default_ttl=3)
    cache.set("user_1", {"name": "Alice", "age": 30})
    cache.set("user_2", {"name": "Bob", "age": 25})

    print(f"✅ Получено user_1: {cache.get('user_1')}")
    print(f"✅ Получено user_2: {cache.get('user_2')}")
    print(f"🔍 Проверка существования key_3: {cache.has('key_3')}")

    print("\n⏳ Ждём 4 секунды для истечения TTL...")
    time.sleep(4)

    print(f"⏰ После истечения TTL: {cache.get('user_1')}")
    print("✅ Тест кэширования пройден!")


if __name__ == "__main__":
    main()
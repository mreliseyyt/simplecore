"""
Простой тест для проверки импорта библиотеки
"""

def test_import():
    """Проверяем, что библиотека импортируется без ошибок"""
    try:
        import pysimplecore
        assert hasattr(pysimplecore, '__version__')
    except ImportError:
        assert False, "Не удалось импортировать pysimplecore"
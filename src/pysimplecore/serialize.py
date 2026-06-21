import json
import pickle
from typing import Any


class Serializer:

    @staticmethod
    def to_json(obj: Any, indent: int = 2) -> str:
        try:
            return json.dumps(obj, indent=indent, ensure_ascii=False)
        except TypeError:
            if hasattr(obj, '__dict__'):
                return json.dumps(obj.__dict__, indent=indent, ensure_ascii=False)
            raise

    @staticmethod
    def from_json(json_str: str) -> Any:
        return json.loads(json_str)

    @staticmethod
    def to_pickle(obj: Any, filepath: str) -> None:
        with open(filepath, 'wb') as f:
            pickle.dump(obj, f)

    @staticmethod
    def from_pickle(filepath: str) -> Any:
        with open(filepath, 'rb') as f:
            return pickle.load(f)

    @staticmethod
    def to_yaml(obj: Any, filepath: str) -> None:
        """Сохранить в YAML (требуется PyYAML)"""
        try:
            import yaml
            with open(filepath, 'w', encoding='utf-8') as f:
                yaml.dump(obj, f, allow_unicode=True)
        except ImportError:
            raise ImportError("Установите PyYAML: pip install pyyaml")
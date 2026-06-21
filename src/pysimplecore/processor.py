
from typing import Any, Dict, List, Callable
from collections import defaultdict


class DataProcessor:

    @staticmethod
    def filter_by_key(data: List[Dict], key: str, value: Any) -> List[Dict]:
        return [item for item in data if item.get(key) == value]

    @staticmethod
    def group_by_key(data: List[Dict], key: str) -> Dict[Any, List[Dict]]:
        result = defaultdict(list)
        for item in data:
            result[item.get(key)].append(item)
        return dict(result)

    @staticmethod
    def pluck(data: List[Dict], key: str) -> List[Any]:
        return [item.get(key) for item in data if key in item]

    @staticmethod
    def unique(data: List[Any]) -> List[Any]:
        return list(dict.fromkeys(data))

    @staticmethod
    def sort_by_key(data: List[Dict], key: str, reverse: bool = False) -> List[Dict]:
        return sorted(data, key=lambda x: x.get(key), reverse=reverse)

    @staticmethod
    def map_values(data: List[Dict], key: str, func: Callable) -> List[Dict]:
        result = []
        for item in data:
            new_item = item.copy()
            if key in new_item:
                new_item[key] = func(new_item[key])
            result.append(new_item)
        return result
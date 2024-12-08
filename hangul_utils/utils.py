import re
from typing import Any, Dict, List, Union


def is_number(value: Any) -> bool:
    # 숫자형인지 확인
    if isinstance(value, bool):
        return False
    elif isinstance(value, (int, float, complex)):
        return True
    elif isinstance(value, str):
        try:
            float(value)
            return True
        except ValueError:
            return False
    return False


def split_by_key(key: str = "") -> List[str]:
    """키를 한글, 영문, 숫자 단위로 분리"""
    if not key:
        return []
    pattern = r"[ㄱ-힣a-zA-Z0-9]+"
    return re.findall(pattern, key)


def get_nested_property(key: Union[List[str], str], obj: Dict = None) -> Any:
    """중첩된 객체에서 키에 해당하는 값을 가져옴"""
    if obj is None:
        obj = {}

    _key = split_by_key(key) if isinstance(key, str) else key

    if not _key:
        return None

    result = obj
    for k in _key:
        if not isinstance(result, dict):
            return None
        result = result.get(k)

    return result


def zero_pad(string: Union[int, str], length: int = 0, pad: str = "0") -> str:
    """문자열 앞에 0을 채움"""
    result = str(string)
    pad_string = str(pad)

    while len(result) < length:
        result = pad_string + result

    return result


def chunk_at_end(value: str = "", n: int = 1) -> List[str]:
    """문자열을 뒤에서부터 n개씩 자름"""
    result = []
    start = len(value)

    while (start := start - n) > 0:
        result.append(value[start : start + n])

    if start > -n:
        result.append(value[: start + n])

    return result


def make_percent_by_object(obj: Dict) -> Dict[str, float]:
    """객체의 값들을 백분율로 변환"""
    result = {}
    total = sum(v for v in obj.values() if is_number(v))

    if total == 0:
        return result

    for key, value in obj.items():
        if is_number(value):
            result[key] = round((value / total) * 100, 2)

    return result


def reverse_by_object(obj: Union[Dict, List]) -> Dict:
    """객체의 키와 값을 뒤집음"""
    if isinstance(obj, list):
        return {str(v): str(k) for k, v in enumerate(obj)}
    return {str(v): k for k, v in obj.items()}


def reverse_by_array(array: List) -> List:
    """배열을 재귀적으로 뒤집음"""
    result = []

    for item in array:
        if isinstance(item, list):
            item = reverse_by_array(item)
        result.insert(0, item)

    return result

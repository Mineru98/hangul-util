from typing import Any, Dict, List, Optional, Union

from hangul_utils.utils import get_nested_property, split_by_key


class SortKey:
    """Python의 sort를 위한 비교 키 클래스"""

    def __init__(self, obj: Any, compare_func: callable):
        self.obj = obj
        self.compare_func = compare_func

    def __lt__(self, other: "SortKey") -> bool:
        return self.compare_func(self.obj, other.obj) < 0

    def __gt__(self, other: "SortKey") -> bool:
        return self.compare_func(self.obj, other.obj) > 0

    def __eq__(self, other: "SortKey") -> bool:
        return self.compare_func(self.obj, other.obj) == 0

    def __le__(self, other: "SortKey") -> bool:
        return self.compare_func(self.obj, other.obj) <= 0

    def __ge__(self, other: "SortKey") -> bool:
        return self.compare_func(self.obj, other.obj) >= 0


def __is_hangul_syllable(char: str) -> bool:
    """완성형 한글인지 확인하는 함수"""
    if not isinstance(char, str) or not char:
        return False
    code = ord(char[0])
    return 0xAC00 <= code <= 0xD7A3


def __is_hangul_jamo(char: str) -> bool:
    """한글 자음/모음인지 확인하는 함수"""
    if not isinstance(char, str) or not char:
        return False
    code = ord(char[0])
    return 0x3131 <= code <= 0x318E


def __base_compare(
    str1: Union[str, int, Dict], str2: Union[str, int, Dict], order_asc: bool
) -> int:
    """문자열 비교 기본 함수"""
    # Dict 타입인 경우 키 값들을 정렬하여 비교
    if isinstance(str1, dict) and isinstance(str2, dict):
        str1_keys = sorted(str1.keys())
        str2_keys = sorted(str2.keys())

        for key in str1_keys:
            if key not in str2_keys:
                return -1 if order_asc else 1
            result = __base_compare(str1[key], str2[key], order_asc)
            if result != 0:
                return result

        if len(str1_keys) < len(str2_keys):
            return -1 if order_asc else 1
        return 0

    # 기존 정수 처리
    if isinstance(str1, int):
        str1 = str(str1)
    if isinstance(str2, int):
        str2 = str(str2)

    # 숫자는 항상 먼저
    if str1.isdigit() and not str2.isdigit():
        return -1 if order_asc else 1
    if not str1.isdigit() and str2.isdigit():
        return 1 if order_asc else -1

    # 완성형 한글 우선, 그 다음 자음/모음, 마지막 영문
    str1_syllable = __is_hangul_syllable(str1)
    str2_syllable = __is_hangul_syllable(str2)
    str1_jamo = __is_hangul_jamo(str1)
    str2_jamo = __is_hangul_jamo(str2)

    # 완성형 한글 vs 나머지
    if str1_syllable and not str2_syllable:
        return -1 if order_asc else 1
    if not str1_syllable and str2_syllable:
        return 1 if order_asc else -1

    # 자음/모음 vs 영문
    if str1_jamo and not (str2_syllable or str2_jamo):
        return -1 if order_asc else 1
    if not (str1_syllable or str1_jamo) and str2_jamo:
        return 1 if order_asc else -1

    # 같은 종류의 문자일 경우 일반 비교
    if order_asc:
        return -1 if str1 < str2 else 1 if str1 > str2 else 0
    return -1 if str2 < str1 else 1 if str2 > str1 else 0


def __base_sort_by(
    array: List[Any] = [],
    compare: Optional[Union[List[str], str]] = None,
    order_asc: bool = True,
) -> List[Any]:
    """배열 정렬 기본 함수"""

    def compare_func(a: Any, b: Any) -> int:
        # compare가 있는 경우 해당 키의 value로 정렬
        if isinstance(compare, list):
            keys = [split_by_key(x) for x in compare]
            for key in keys:
                val1 = get_nested_property(key, a)
                val2 = get_nested_property(key, b)
                if val1 != val2:
                    return -1 if val1 < val2 else 1
            return 0

        if compare:
            keys = split_by_key(compare)
            val1 = get_nested_property(keys, a)
            val2 = get_nested_property(keys, b)
            return -1 if val1 < val2 else 1 if val1 > val2 else 0

        # compare가 없는 경우 key 순서대로 정렬
        if isinstance(a, dict) and isinstance(b, dict):
            a_keys = sorted(a.keys())
            b_keys = sorted(b.keys())
            for key in a_keys:
                if key not in b_keys:
                    return -1 if order_asc else 1
                if a[key] != b[key]:
                    return -1 if a[key] < b[key] else 1
            return 0

        return __base_compare(a, b, order_asc)

    return sorted(array, key=lambda x: SortKey(x, compare_func))


def sort_by_asc(
    array: List[Any] = None,
    compare: Optional[Union[List[str], str]] = None,
) -> List[Any]:
    """오름차순 정렬"""
    return __base_sort_by(array, compare, True)


def sort_by_desc(
    array: List[Any] = None,
    compare: Optional[Union[List[str], str]] = None,
) -> List[Any]:
    """내림차순 정렬"""
    return __base_sort_by(array, compare, False)


def sort_by_groups(
    array: List[Any] = None,
    groups: List[Union[int, str]] = None,
    order_asc: bool = True,
    compare: Optional[str] = None,
) -> List[Any]:
    """그룹별 정렬

    Args:
        array: 정렬할 배열
        groups: 그룹 순서
        order_asc: 오름차순 여부
        compare: 비교할 키

    Returns:
        정렬된 배열
    """
    if array is not None and any(isinstance(x, dict) for x in array):
        raise TypeError("배열에 딕셔너리 타입이 포함되어 있습니다")
    if array is None:
        array = []
    if groups is None:
        groups = []

    # 그룹 순서를 인덱스로 변환
    group_order = {str(v): i for i, v in enumerate(groups)}

    def sort_by_groups_func(a: Any, b: Any) -> int:
        keys = split_by_key(compare) if compare else None
        a_value = get_nested_property(keys, a) if keys else a
        b_value = get_nested_property(keys, b) if keys else b

        status1 = group_order.get(str(a_value), -1)
        status2 = group_order.get(str(b_value), -1)

        if status1 == status2:
            return __base_compare(a_value, b_value, order_asc)
        if status1 == -1:
            return 1 if order_asc else -1
        if status2 == -1:
            return -1 if order_asc else 1

        condition1 = status1 - status2 if order_asc else status2 - status1
        condition2 = __base_compare(a_value, b_value, order_asc)

        return condition1 or condition2 or 0

    return sorted(array, key=lambda x: SortKey(x, sort_by_groups_func))

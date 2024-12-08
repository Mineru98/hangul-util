from typing import Dict, List, Literal, Union

from hangul_utils.constant import (
    CHO_HANGUL,
    CHO_PERIOD,
    HANGUL_START_CHARCODE,
    JONG_COMPLETE_HANGUL,
    JONG_HANGUL,
    JONG_PERIOD,
    JUNG_COMPLETE_HANGUL,
    JUNG_HANGUL,
)
from hangul_utils.is_hangul import is_hangul_by_code


def divide(
    word: str = "",
    is_split: bool = True,
    result_type: Literal["list", "dict", "str", "index"] = "list",
) -> Union[List[str], Dict, str]:
    """한글 문자를 자모음으로 분리"""

    word_code = ord(word[0])
    char_code = word_code - HANGUL_START_CHARCODE

    if not is_hangul_by_code(word_code):
        return [word[0]]

    cho_index = char_code // CHO_PERIOD
    jung_index = (char_code % CHO_PERIOD) // JONG_PERIOD
    jong_index = char_code % JONG_PERIOD

    cho = CHO_HANGUL[cho_index] if cho_index < len(CHO_HANGUL) else ""
    jung = JUNG_HANGUL[jung_index] if jung_index < len(JUNG_HANGUL) else ""
    jong = JONG_HANGUL[jong_index] if jong_index < len(JONG_HANGUL) else ""

    # 더 세분하게 분리
    divided_jung = divide_by_jung(jung) if is_split else jung
    divided_jong = divide_by_jong(jong) if is_split else jong

    if result_type == "index":
        return {"cho": cho_index, "jung": jung_index, "jong": jong_index}

    if result_type == "dict":
        return {"cho": cho, "jung": divided_jung, "jong": divided_jong}

    if result_type == "str":
        return cho + divided_jung + divided_jong

    return list(cho + divided_jung + divided_jong)


def divide_hangul_by_groups(
    word: str = "", is_split: bool = True, result_type: str = "list"
) -> List:
    """문자열의 각 글자를 자모음으로 분리"""
    return [divide(char, is_split, result_type) for char in str(word)]


def divide_hangul(word: str = "", is_split: bool = True) -> List[str]:
    """문자열을 자모음으로 분리"""
    divided = []
    for char in str(word):
        result = divide(char, is_split, "str")
        divided.extend(list(result))
    return divided


def divide_by_jung(jung: str) -> str:
    """중성을 더 작은 단위로 분리"""
    return JUNG_COMPLETE_HANGUL.get(jung, jung)


def divide_by_jong(jong: str) -> str:
    """종성을 더 작은 단위로 분리"""
    return JONG_COMPLETE_HANGUL.get(jong, jong)

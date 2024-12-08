from typing import List, Union

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
from hangul_utils.is_cho import is_cho
from hangul_utils.is_hangul import is_hangul_by_code
from hangul_utils.is_jong import is_jong
from hangul_utils.is_jung import is_jung
from hangul_utils.utils import reverse_by_object

# 메모이제이션을 위한 캐시
_from_char_code_memo = {}


def combine_by_code(cho: int = 0, jung: int = 0, jong: int = 0) -> str:
    """초성, 중성, 종성 인덱스로 한글 문자 생성"""
    hangul_code = HANGUL_START_CHARCODE + cho * CHO_PERIOD + jung * JONG_PERIOD + jong

    if not is_hangul_by_code(hangul_code):
        return ""

    if hangul_code not in _from_char_code_memo:
        _from_char_code_memo[hangul_code] = chr(hangul_code)

    return _from_char_code_memo[hangul_code]


def combine(cho: str = "", jung: str = "", jong: str = "") -> str:
    """초성, 중성, 종성 문자로 한글 문자 생성"""
    combine_jung = combine_by_jung(jung)
    combine_jong = combine_by_jong(jong)

    cho_index = CHO_HANGUL.index(cho) if cho in CHO_HANGUL else -1
    jung_index = JUNG_HANGUL.index(combine_jung) if combine_jung in JUNG_HANGUL else -1
    jong_index = JONG_HANGUL.index(combine_jong) if combine_jong in JONG_HANGUL else -1

    if -1 in (cho_index, jung_index, jong_index):
        return cho or combine_jung or combine_jong

    return combine_by_code(cho_index, jung_index, jong_index)


def combine_loop(word_list: List[str]) -> str:
    """문자 리스트를 순회하며 한글로 조합"""
    index = 0
    result = []

    while index < len(word_list):
        first = word_list[index]
        index += 1

        cho = first if is_cho(first) else ""

        jung = (
            word_list[index]
            if cho and index < len(word_list) and is_jung(word_list[index])
            else ""
        )
        if jung:
            index += 1

        if not (cho and jung):
            result.append(first)
            continue

        # 중성 결합 확인
        sub_jung = ""
        if index < len(word_list):
            temp_jung = combine_by_jung(jung + word_list[index])
            if temp_jung in JUNG_COMPLETE_HANGUL:
                sub_jung = word_list[index]
                index += 1

        # 종성 확인
        jong = ""
        if index < len(word_list) and is_jong(word_list[index]):
            if index + 1 >= len(word_list) or not is_jung(word_list[index + 1]):
                jong = word_list[index]
                index += 1

        # 종성 결합 확인
        sub_jong = ""
        if index < len(word_list):
            temp_jong = combine_by_jong(jong + word_list[index])
            if temp_jong in JONG_COMPLETE_HANGUL and (
                index + 1 >= len(word_list) or not is_jung(word_list[index + 1])
            ):
                sub_jong = word_list[index]
                index += 1

        result.append(combine(cho, jung + sub_jung, jong + sub_jong))

    return "".join(result)


def combine_hangul(text: Union[str, List[Union[str, List[str]]]] = "") -> str:
    """한글 자모음을 결합하여 완성형 한글로 변환"""
    if isinstance(text, str):
        word = list(text)
    else:
        word = text

    result = []
    temp = []

    for item in word:
        if isinstance(item, str):
            temp.extend(list(item))
        else:
            result.append(combine_loop(temp) + combine_loop(list("".join(item))))
            temp = []

    result.append(combine_loop(temp))
    return "".join(result)


def combine_by_jung(jung: str) -> str:
    """중성 자모음 결합"""
    reverse_jung_complete = reverse_by_object(JUNG_COMPLETE_HANGUL)
    return reverse_jung_complete.get(jung, jung)


def combine_by_jong(jong: str) -> str:
    """종성 자모음 결합"""
    reverse_jong_complete = reverse_by_object(JONG_COMPLETE_HANGUL)
    return reverse_jong_complete.get(jong, jong)

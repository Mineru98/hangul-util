import re
from typing import Dict, List, Literal, Union

from hangul_utils.utils import make_percent_by_object

LocalType = Literal["ko", "en", "number", "special", "etc"]

# 언어별 정규식 패턴
LANGUAGE_REGEXP: Dict[LocalType, re.Pattern] = {
    "ko": re.compile(r"^[가-힣|ㄱ-ㅎ|ㅏ-ㅣ|\s]+$"),
    "en": re.compile(r"^[a-zA-Z|\s]+$"),
    "number": re.compile(r"^[0-9]+$"),
    "special": re.compile(
        r"^[\`\~\!\@\#\$\%\^\&\*\(\)\_\+\-\=\\\|\{\}\[\]\;\:\'\"\<\,\.\>\/\?\s]+$"
    ),
    "etc": re.compile(r".*"),
}


def get_local(word: str = "") -> LocalType:
    """문자열의 언어 타입을 반환

    Args:
        word: 검사할 문자열

    Returns:
        언어 타입 ("ko", "en", "number", "special", "etc")
    """
    if LANGUAGE_REGEXP["special"].match(word):
        return "special"
    if LANGUAGE_REGEXP["ko"].match(word):
        return "ko"
    if LANGUAGE_REGEXP["en"].match(word):
        return "en"
    if LANGUAGE_REGEXP["number"].match(word):
        return "number"
    return "etc"


def get_local_by_groups(
    word: str = "",
    is_percent: bool = False,
) -> Union[List[LocalType], Dict[LocalType, float]]:
    """문자열의 각 문자별 언어 타입을 반환

    Args:
        word: 검사할 문자열
        is_percent: 백분율로 반환할지 여부

    Returns:
        언어 타입 리스트 또는 언어별 비율
    """
    count_object = {
        "ko": 0,
        "en": 0,
        "number": 0,
        "special": 0,
        "etc": 0,
    }

    if is_percent:
        for char in word:
            language = get_local(char)
            count_object[language] += 1
        return make_percent_by_object(count_object)

    return [get_local(char) for char in word]

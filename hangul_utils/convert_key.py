from typing import Literal

from hangul_utils.combine import combine_hangul
from hangul_utils.constant import KEY_MAPS
from hangul_utils.divide import divide_hangul
from hangul_utils.utils import reverse_by_object

# KEY_MAPS의 역방향 매핑 생성
REVERSE_MAPS = reverse_by_object(KEY_MAPS)


def to_ko(english: str = "") -> str:
    """영문을 한글 자모음으로 변환"""
    return "".join(REVERSE_MAPS.get(char, char) for char in str(english))


def to_en(korean: str = "") -> str:
    """한글 자모음을 영문으로 변환"""
    return "".join(KEY_MAPS.get(char, char) for char in str(korean))


def convert_key(
    word: str = "",
    to_language: Literal["ko", "en"] = "ko",
    is_combine: bool = True,
) -> str:
    """키보드 입력을 변환

    Args:
        word: 변환할 문자열
        to_language: 변환할 언어 ("ko" 또는 "en")
        is_combine: 한글로 변환시 자모음 결합 여부

    Returns:
        변환된 문자열
    """
    hangul = "".join(divide_hangul(word) if is_combine else list(str(word)))

    # 한타로 변환
    if to_language == "ko":
        return combine_hangul(to_ko(hangul)) if is_combine else to_ko(hangul)

    # 영타로 변환
    if to_language == "en":
        return to_en(hangul)

    return word

from hangul_utils.constant import JONG_COMPLETE_HANGUL


def is_cho_by_char(cho: str = "") -> bool:
    """한 글자가 초성인지 확인"""
    if not cho:
        return False

    # 초성 범위: 0x3131-0x314E
    code = ord(cho[0])
    return 0x3131 <= code <= 0x314E and cho not in JONG_COMPLETE_HANGUL


def is_cho(word: str = "") -> bool:
    """문자열이 모두 초성인지 확인"""
    if not word:
        return False
    return all(is_cho_by_char(char) for char in word)


def is_cho_by_groups(word: str = "") -> list:
    """문자열의 각 글자가 초성인지 여부를 리스트로 반환"""
    return [is_cho_by_char(char) for char in str(word)]

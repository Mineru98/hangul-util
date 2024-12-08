from hangul_utils.constant import JONG_END_CHARCODE, JONG_START_CHARCODE


def is_jong_by_code(jong: int = 0) -> bool:
    """유니코드가 종성 범위에 있는지 확인"""
    return JONG_START_CHARCODE <= jong <= JONG_END_CHARCODE


def is_jong(word: str = "") -> bool:
    """문자열이 모두 종성인지 확인"""
    if not word:
        return False
    return all(is_jong_by_code(ord(char)) for char in word)


def is_jong_by_groups(word: str = "") -> list:
    """문자열의 각 글자가 종성인지 여부를 리스트로 반환"""
    return [is_jong_by_code(ord(char)) for char in str(word)]

from hangul_utils.constant import JUNG_END_CHARCODE, JUNG_START_CHARCODE


def is_jung_by_code(jung: int = 0) -> bool:
    """유니코드가 중성 범위에 있는지 확인"""
    return JUNG_START_CHARCODE <= jung <= JUNG_END_CHARCODE


def is_jung(word: str = "") -> bool:
    """문자열이 모두 중성인지 확인"""
    if not word:
        return False
    return all(is_jung_by_code(ord(char)) for char in word)


def is_jung_by_groups(word: str = "") -> list:
    """문자열의 각 글자가 중성인지 여부를 리스트로 반환"""
    return [is_jung_by_code(ord(char)) for char in str(word)]

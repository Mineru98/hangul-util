from hangul_utils.constant import HANGUL_END_CHARCODE, HANGUL_START_CHARCODE


def is_hangul_by_code(hangul: int = 0) -> bool:
    """유니코드가 한글 범위에 있는지 확인"""
    return HANGUL_START_CHARCODE <= hangul <= HANGUL_END_CHARCODE


def is_hangul(word: str = "") -> bool:
    """문자열이 모두 한글인지 확인"""
    if not word:
        return False
    return all(is_hangul_by_code(ord(char)) for char in word)


def is_hangul_by_groups(word: str = "") -> list:
    """문자열의 각 글자가 한글인지 여부를 리스트로 반환"""
    return [is_hangul_by_code(ord(char)) for char in str(word)]

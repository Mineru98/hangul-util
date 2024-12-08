from typing import Optional

from hangul_utils.constant import JOSA_LIST


def josa(letter: str = "", _josa: str = "이") -> str:
    """조사 선택

    Args:
        letter: 단어
        _josa: 조사 ("이/가", "은/는" 등)

    Returns:
        선택된 조사
    """
    if not letter:
        return _josa

    # 받침 유무 확인
    has_jong = (ord(letter[-1]) - ord("가")) % 28 > 0
    josa_index = 0 if has_jong else 1

    # 대괄호 제거
    josa_str = _josa.replace("[", "").replace("]", "")

    # 조사 케이스 찾기
    josa_case = get_josa_case(josa_str.split("/")[0]) or josa_str

    return (josa_case.split("/") + [josa_str])[josa_index]


def format_josa(letter: str = "") -> str:
    """문장의 모든 조사를 처리

    Args:
        letter: 문장

    Returns:
        조사가 처리된 문장

    Example:
        >>> format_josa("오늘[은/는] 사과[이/가]")
        "오늘은 사과가"
    """
    import re

    def replace_josa(match: re.Match) -> str:
        word = match.group(0)
        return word[0] + josa(word[0], word[1:])

    pattern = r"[가-힣]\[[가-힣]+\/[가-힣]+\]"
    return re.sub(pattern, replace_josa, letter)


def get_josa_case(josa_str: str = "") -> Optional[str]:
    """조사 케이스 찾기"""
    return JOSA_LIST.get(josa_str)

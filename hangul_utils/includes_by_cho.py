import re

from hangul_utils.combine import combine_by_code
from hangul_utils.constant import CHO_HANGUL


def make_regex_by_cho(search: str = "") -> re.Pattern:
    """
    초성 기준으로 정규식을 생성
    :param search: 검색 문자열
    :return: 초성 기반 정규식
    """
    regex = search
    for index, cho in enumerate(CHO_HANGUL):
        start = combine_by_code(index, 0, 0)
        end = combine_by_code(index + 1, 0, -1)
        regex = re.sub(re.escape(cho), f"[{start}-{end}]", regex)
    return re.compile(f"({regex})", re.UNICODE)


def includes_by_cho(search: str = "", word: str = "") -> bool:
    """
    초성 기반으로 단어가 포함되는지 확인
    :param search: 검색 문자열
    :param word: 대상 단어
    :return: 포함 여부 (True/False)
    """
    regex = make_regex_by_cho(search)
    return bool(regex.search(word))

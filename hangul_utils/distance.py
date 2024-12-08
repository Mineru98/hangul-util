from typing import Dict, List, Optional

from hangul_utils.divide import divide_hangul
from hangul_utils.sort_hangul import sort_by_asc


def get_distance(first: str, second: str) -> int:
    """레벤슈타인 거리 계산 (반복적 구현)

    Args:
        first: 첫 번째 문자열
        second: 두 번째 문자열

    Returns:
        두 문자열 간의 레벤슈타인 거리
    """
    m, n = len(first), len(second)

    # DP 테이블 생성
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 초기화: 한 문자열이 비어있을 때
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # DP 테이블 채우기
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if first[i - 1] == second[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # 같은 문자
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]  # 삭제  # 삽입  # 대체
                )

    return dp[m][n]


def correct_by_distance(
    word: str,
    word_list: List[str],
    is_split: bool = True,
    distance: Optional[int] = None,
    max_slice: int = 10,
) -> List[str]:
    """주어진 단어와 가장 유사한 단어들을 찾음

    Args:
        word: 기준 단어
        word_list: 비교할 단어 목록
        is_split: 한글 분리 여부
        distance: 거리
        max_slice: 최대 반환 개수

    Returns:
        유사도가 높은 순으로 정렬된 단어 목록
    """
    if distance is None:
        distance = max(len(word) / 2, 2)

    min_dist = []
    divided_word = "".join(divide_hangul(word, True))

    for candidate in word_list:
        dist = (
            get_distance(divided_word, "".join(divide_hangul(candidate, True)))
            if is_split
            else get_distance(word, candidate)
        )

        if dist <= distance:
            min_dist.append({"dist": dist, "word": candidate})

    return [item["word"] for item in sort_by_asc(min_dist, "dist")[:max_slice]]

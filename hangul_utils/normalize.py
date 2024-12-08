from typing import Dict

from hangul_utils.constant import NORMALIZE_CHO, NORMALIZE_JONG, NORMALIZE_JUNG
from hangul_utils.divide import divide_hangul_by_groups


def normalize(text: str, is_space: bool = True) -> str:
    """한글을 로마자로 변환

    Args:
        text: 변환할 텍스트
        is_space: 음절 사이에 공백을 넣을지 여부

    Returns:
        변환된 텍스트
    """
    divided = divide_hangul_by_groups(text, is_split=False, result_type="index")

    space = " " if is_space else ""

    result = []
    for hangul in divided:
        if isinstance(hangul, Dict):
            char = (
                NORMALIZE_CHO[hangul["cho"]]
                + NORMALIZE_JUNG[hangul["jung"]]
                + NORMALIZE_JONG[hangul["jong"]]
            )
            result.append(char + space if char else hangul)
        elif isinstance(hangul, list):
            result.append(" ".join(hangul))
        else:
            result.append(hangul)
    return " ".join("".join(result).split()).strip()

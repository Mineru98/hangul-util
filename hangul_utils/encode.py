import base64
import json
import random
from typing import Any
from urllib.parse import quote, unquote

from hangul_utils.utils import chunk_at_end


def _escape(text: str) -> str:
    """문자열 이스케이프"""
    return quote(text)


def _chunk_and_join(text: str, n: int) -> str:
    """문자열을 n개씩 나누고 다시 합침"""
    return "".join(chunk_at_end("".join(chunk_at_end(text)), n))


def _add_random_char(text: str) -> str:
    """3글자마다 랜덤 문자 추가"""
    result = []
    for i, char in enumerate(text):
        result.append(char)
        if i % 3 == 0:
            result.append(str(random.randint(0, 5)))
    return "".join(result)


def _split_and_swap(text: str) -> str:
    """문자열을 반으로 나누고 순서 바꾸기"""
    mid = len(text) // 2
    return text[mid:] + text[:mid]


# 인코딩 함수 목록
_encoders = [
    _escape,
    lambda t: _chunk_and_join(t, 3),
    lambda t: _chunk_and_join(t, 4),
    lambda t: "".join(chunk_at_end(t)),
    _add_random_char,
    _split_and_swap,
]


def encode(text: Any = "", level: int = 0) -> str:
    """문자열을 여러 단계로 인코딩

    Args:
        text: 인코딩할 데이터
        level: 인코딩 레벨

    Returns:
        인코딩된 문자열
    """
    encoder_index = random.randint(0, len(_encoders) - 1)
    if level % 3 == 0:
        encoded = base64.b64encode(quote(json.dumps(text)).encode()).decode()
    else:
        encoded = _encoders[encoder_index](text)

    if level == 5:
        return str(encoder_index) + base64.b64encode(quote(encoded).encode()).decode()

    prefix = str(encoder_index) if level % 2 == 1 else ""
    suffix = str(encoder_index) if level % 2 == 0 else ""

    return encode(prefix + encoded + suffix, level + 1)


def decode(text: str = "", level: int = 5) -> Any:
    """인코딩된 문자열을 디코딩

    Args:
        text: 디코딩할 문자열
        level: 디코딩 레벨

    Returns:
        디코딩된 데이터
    """
    if level % 2 == 1:
        parts = [text[1:], int(text[0])]
    else:
        parts = [text[:-1], int(text[-1])]

    decoded = unquote(base64.b64decode(parts[0]).decode()) if level == 5 else parts[0]

    result = (
        json.loads(unquote(base64.b64decode(decoded).decode()))
        if level % 3 == 0
        else _encoders[parts[1]](decoded)
    )

    return result if level == 0 else decode(result, level - 1)

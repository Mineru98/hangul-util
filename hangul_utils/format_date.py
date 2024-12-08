import re
from datetime import datetime
from typing import Optional, Union

from hangul_utils.constant import WEEK_DAY
from hangul_utils.utils import zero_pad

# 날짜 포맷 패턴
DATE_REGEX = re.compile(r"Y{2,4}|M{1,2}|D{1,2}|d{1,2}|H{1,2}|m{1,2}|s{1,2}")


def format_date(
    date: Optional[Union[str, datetime]] = None,
    format_style: str = "YYYY년MM월DD일 HH시mm분ss초",
) -> str:
    """날짜를 지정된 형식으로 포맷팅

    Args:
        date: 날짜 (문자열 또는 datetime 객체)
        format_style: 포맷 스타일

    Returns:
        포맷팅된 날짜 문자열

    Examples:
        YY: 22, YYYY: 2022
        M: 2, MM: 02
        D: 2, DD: 02
        d: 3, dd: '화'
        H: 2, HH: 02
        m: 2, mm: 02
        s: 2, ss: 02
    """
    if date is None:
        date = datetime.now()
    elif isinstance(date, str):
        date = datetime.fromisoformat(date)

    year = zero_pad(date.year, 4)
    month = date.month
    day = date.day
    hour = date.hour
    minute = date.minute
    second = date.second
    week = date.weekday()

    def matcher(match: re.Match) -> str:
        pattern = match.group()
        if pattern == "YY":
            return year[-2:]
        elif pattern == "YYYY":
            return year
        elif pattern == "M":
            return str(month)
        elif pattern == "MM":
            return zero_pad(month, 2)
        elif pattern == "D":
            return str(day)
        elif pattern == "DD":
            return zero_pad(day, 2)
        elif pattern == "d":
            return str(week)
        elif pattern == "dd":
            return WEEK_DAY[week]
        elif pattern == "H":
            return str(hour)
        elif pattern == "HH":
            return zero_pad(hour, 2)
        elif pattern == "m":
            return str(minute)
        elif pattern == "mm":
            return zero_pad(minute, 2)
        elif pattern == "s":
            return str(second)
        elif pattern == "ss":
            return zero_pad(second, 2)
        return pattern

    result = DATE_REGEX.sub(matcher, format_style)

    # 중복된 접미사 제거 (예: 년년 -> 년)
    result = re.sub(r"(년|월|일|시|분|초{1})(년|월|일|시|분|초{1})+", r"\1", result)

    # 연속된 공백 제거
    result = re.sub(r"\s+", " ", result)

    return result

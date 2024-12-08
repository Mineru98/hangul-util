import re

from hangul_utils.utils import reverse_by_array

FIRST_REGEX = r"(^|\s)?([가-힣]{0,3})?(\s*)"
LAST_REGEX = r"([.,\s]|$)"

# formater 순서를 약간 조정:
# - "입니다" <-> "이다"를 먼저 처리해 더 일반적인 "습니다" <-> "다" 치환보다 우선되도록 함
# - "합니다" -> "다"로 수정
formater = [
    [["습니다"], ["다"]],
    [["주세요"], ["라"]],
    [["입니다"], ["이다"]],
    [["합니다"], ["하다"]],
    [["옵니다"], ["온다"]],
    [["됩니다"], ["된다"]],
    [["갑니다"], ["간다"]],
    [["깁니다"], ["긴다"]],
    [["십니다"], ["신다"]],
    [["랍니다"], ["란다"]],
    [["저는"], ["나는"]],
]


def make_reg_by_formater(array, honorific_to_banmal=True):
    result = []
    for case_list in array:
        for honorific_form in case_list[0]:
            pattern_form = honorific_form
            # 반말->존댓말 변환 시 (reverse_by_array 결과), "다"를 치환할 때 니다 형태 제외하기
            if not honorific_to_banmal:
                # 여기서는 반말->존댓말 변환용 regex를 만들 때 처리
                # case_list[1]에 "습니다"가 있는 경우는 문제 없음
                # case_list[1]에 "다"가 있는 경우는 없음(원본 formater에 없음)
                pass

            regex = re.compile(FIRST_REGEX + pattern_form + LAST_REGEX, re.IGNORECASE)
            for banmal_form in case_list[1]:
                replacement = f"\\1\\2\\3{banmal_form}\\4"
                result.append((regex, replacement))
    return result


BANMAL_REGEX_LIST = make_reg_by_formater(formater, honorific_to_banmal=True)

# 반대로 존댓말로 바꿀 때 (reverse)
reversed_formater = reverse_by_array(formater)
# 여기서는 "다"를 치환할 때 '(?<!니)다'를 사용하도록 함
# reversed_formater에서 ["다"], ["습니다"]] 형태가 존재할 경우 수정
adjusted_formater = []
for case_list in reversed_formater:
    new_case1 = []
    for form_ in case_list[0]:
        if form_ == "다":
            # 다 -> (?<!니)다 패턴 적용
            form_ = r"(?<!니)다"
        new_case1.append(form_)
    adjusted_formater.append([new_case1, case_list[1]])

HONORIFIC_REGEX_LIST = make_reg_by_formater(
    adjusted_formater, honorific_to_banmal=False
)


def to_banmal(string: str) -> str:
    """존댓말을 반말로 변환"""
    result = string
    for regex, replacement in BANMAL_REGEX_LIST:
        result = regex.sub(replacement, result)
    return result


def to_honorific(string: str) -> str:
    """반말을 존댓말로 변환"""
    result = string
    for regex, replacement in HONORIFIC_REGEX_LIST:
        result = regex.sub(replacement, result)
    return result

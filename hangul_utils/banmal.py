import re

from hangul_utils.utils import reverse_by_array

FIRST_REGEX = r"(^|\s)?([가-힣]{0,3})?(\s*)"
LAST_REGEX = r"([.,\s]|$)"

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
            if not honorific_to_banmal:
                pass

            regex = re.compile(FIRST_REGEX + pattern_form + LAST_REGEX, re.IGNORECASE)
            for banmal_form in case_list[1]:
                replacement = f"\\1\\2\\3{banmal_form}\\4"
                result.append((regex, replacement))
    return result


BANMAL_REGEX_LIST = make_reg_by_formater(formater, honorific_to_banmal=True)

reversed_formater = reverse_by_array(formater)
adjusted_formater = []
for case_list in reversed_formater:
    new_case1 = []
    for form_ in case_list[0]:
        if form_ == "다":
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

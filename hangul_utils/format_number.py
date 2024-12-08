from hangul_utils.constant import OVER_DIGIT, number_units, ten_units, thousand_units
from hangul_utils.utils import chunk_at_end, is_number, zero_pad


def format_number(format: int | str | None = ""):
    def formatter(format: int | str | None = ""):
        if not is_number(format):
            return ""

        chunks = list(reversed(list(chunk_at_end(str(format), 4))))
        return " ".join(
            reversed(
                " ".join(
                    f"{int(item)}{thousand_units[index]}"
                    for index, item in enumerate(reversed(chunks))
                    if int(item)
                )
                .strip()
                .split(" ")
            )
        )

    if len(str(format)) > OVER_DIGIT:
        return "범위초과"

    parts = str(format).replace(",", "").split(".") if format else []

    return " 점 ".join(map(formatter, parts)).strip() if parts else ""


def format_number_all(format: int | str | None = ""):
    def formatter(format: int | str | None = ""):
        if not is_number(format):
            return ""

        def convert_chunk(item, index):
            if not int(item):
                return ""

            number_unit = ""
            zero_item = zero_pad(item, 4)

            for i in range(4):
                number = int(zero_item[i])
                if number:
                    unit = ten_units[3 - i]
                    number_unit += (
                        f"{'' if unit and number == 1 else number_units[number]}{unit}"
                    )

            thousand_unit = thousand_units[index] if index < len(thousand_units) else ""
            return f"{number_unit}{thousand_unit}"

        return " ".join(
            reversed(
                " ".join(
                    convert_chunk(item, index)
                    for index, item in enumerate(chunk_at_end(str(format), 4))
                    if int(item)
                )
                .strip()
                .split(" ")
            )
        )

    if len(str(format)) > OVER_DIGIT:
        return "범위초과"

    parts = str(format).replace(",", "").split(".") if format else []

    return " 점 ".join(map(formatter, parts)).strip() if parts else ""

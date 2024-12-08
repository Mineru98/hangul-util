import unittest

from hangul_utils.format_number import format_number, format_number_all


class TestFormatNumber(unittest.TestCase):
    def test_format_number(self):
        self.assertEqual(format_number(1234), "1234")
        self.assertEqual(format_number("12345678"), "1234만 5678")
        self.assertEqual(format_number("0001"), "1")
        self.assertEqual(format_number(123456789), "1억 2345만 6789")
        self.assertEqual(format_number("1234567890123456"), "1234조 5678억 9012만 3456")
        self.assertEqual(format_number("0000000000000001"), "1")
        self.assertEqual(format_number(""), "")
        self.assertEqual(format_number("abc"), "")
        self.assertEqual(format_number(None), "")
        self.assertEqual(format_number(None), "")

    def test_format_number_all(self):
        self.assertEqual(format_number_all(1234), "천이백삼십사")
        self.assertEqual(format_number_all("12345678"), "천이백삼십사만 오천육백칠십팔")
        self.assertEqual(format_number_all("0001"), "일")
        self.assertEqual(
            format_number_all(123456789), "일억 이천삼백사십오만 육천칠백팔십구"
        )
        self.assertEqual(
            format_number_all("1234567890123456"),
            "천이백삼십사조 오천육백칠십팔억 구천십이만 삼천사백오십육",
        )
        self.assertEqual(format_number_all("0000000000000001"), "일")
        self.assertEqual(
            format_number("10000000000000000000000000000000000000000000000000000000"),
            "1000항하사",
        )
        self.assertEqual(
            format_number_all(
                "10000000000000000000000000000000000000000000000000000000"
            ),
            "천항하사",
        )
        self.assertEqual(
            format_number(
                "100000000000000000000000000000000000000000000000000000000000"
            ),
            "1000아승기",
        )
        self.assertEqual(
            format_number_all(
                "100000000000000000000000000000000000000000000000000000000000"
            ),
            "천아승기",
        )
        self.assertEqual(
            format_number(
                "1000000000000000000000000000000000000000000000000000000000000000"
            ),
            "1000나유타",
        )
        self.assertEqual(
            format_number_all(
                "1000000000000000000000000000000000000000000000000000000000000000"
            ),
            "천나유타",
        )
        self.assertEqual(
            format_number(
                "100000000000000000000000000000000000000000000000000000000000000000000000"
            ),
            "1000무량대수",
        )
        self.assertEqual(
            format_number_all(
                "100000000000000000000000000000000000000000000000000000000000000000000000"
            ),
            "천무량대수",
        )
        self.assertEqual(
            format_number_all(
                "1000000000000000000000000000000000000000000000000000000000000000000000000"
            ),
            "범위초과",
        )
        self.assertEqual(format_number("56320563256.1000"), "563억 2056만 3256 점 1000")
        self.assertEqual(
            format_number_all("56320563256.1000"),
            "오백육십삼억 이천오십육만 삼천이백오십육 점 천",
        )
        self.assertEqual(
            format_number("42,563,205,632.1212"), "425억 6320만 5632 점 1212"
        )
        self.assertEqual(
            format_number_all("42,563,205,632.1212"),
            "사백이십오억 육천삼백이십만 오천육백삼십이 점 천이백십이",
        )
        self.assertEqual(format_number_all("400.12"), "사백 점 십이")
        self.assertEqual(format_number_all("400."), "사백 점")
        self.assertEqual(format_number_all("."), "점")
        self.assertEqual(format_number_all(""), "")
        self.assertEqual(format_number_all("abc"), "")
        self.assertEqual(format_number_all(None), "")
        self.assertEqual(format_number_all(None), "")


if __name__ == "__main__":
    unittest.main()

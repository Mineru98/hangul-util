import unittest
from datetime import datetime

from hangul_utils.format_date import format_date


class TestFormatDate(unittest.TestCase):
    def setUp(self):
        self.date = "2022-02-22 22:22:22"

    def test_default_format_with_date(self):
        """formatStyle 기본값 - datetime 테스트"""
        result = format_date(datetime.fromisoformat(self.date))
        self.assertEqual(result, "2022년02월22일 22시22분22초")

    def test_default_format_with_string(self):
        """formatStyle 기본값 - String 테스트"""
        result = format_date(self.date)
        self.assertEqual(result, "2022년02월22일 22시22분22초")

    def test_custom_format_time_year_month(self):
        """HH:mm:ss YYYY년 MM월 포맷 테스트"""
        result = format_date(self.date, "HH:mm:ss YYYY년 MM월")
        self.assertEqual(result, "22:22:22 2022년 02월")

    def test_custom_format_full_date_with_weekday(self):
        """YYYY년 MM월 DD일 dd요일 HH:mm:ss 포맷 테스트"""
        result = format_date(self.date, "YYYY년 MM월 DD일 dd요일 HH:mm:ss")
        print("result", result)
        self.assertEqual(result, "2022년 02월 22일 화요일 22:22:22")

    def test_custom_format_date_time(self):
        """YYYY-MM-DD HH:mm:ss 포맷 테스트"""
        result = format_date(self.date, "YYYY-MM-DD HH:mm:ss")
        self.assertEqual(result, "2022-02-22 22:22:22")


if __name__ == "__main__":
    unittest.main()

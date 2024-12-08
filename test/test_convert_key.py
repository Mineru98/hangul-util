import unittest

from hangul_utils.convert_key import convert_key


class TestConvertKey(unittest.TestCase):
    def test_convert_to_english(self):
        self.assertEqual(
            convert_key("안뇽 안뇽 그렇구만!", "en"), "dkssyd dkssyd rmfjgrnaks!"
        )

    def test_convert_to_korean(self):
        self.assertEqual(
            convert_key("dkssyd dkssyd rmfjgrnaks!", "ko"), "안뇽 안뇽 그렇구만!"
        )

    def test_convert_to_korean_no_combine(self):
        self.assertEqual(
            convert_key("dkssyd dkssyd rmfjgrnaks!", "ko", False),
            "ㅇㅏㄴㄴㅛㅇ ㅇㅏㄴㄴㅛㅇ ㄱㅡㄹㅓㅎㄱㅜㅁㅏㄴ!",
        )

    def test_hello_world(self):
        self.assertEqual(convert_key("ㅗ디ㅣㅐ 재깅!", "en"), "hello world!")

    def test_hello_world_korean(self):
        self.assertEqual(convert_key("hello world!", "ko"), "ㅗ디ㅣㅐ 재깅!")

    def test_invalid_language(self):
        self.assertEqual(
            convert_key("안뇽 안뇽 그렇구만!", "special"), "안뇽 안뇽 그렇구만!"
        )

    def test_performance_english(self):
        input_text = "ㅗㄷㅣㅣㅐ ㅈㅐㄱㅣㅇ!" * 1000000
        expected = "hello world!" * 1000000
        self.assertEqual(convert_key(input_text, "en"), expected)

    def test_performance_korean(self):
        input_text = "hello world!" * 1000000
        expected = "ㅗㄷㅣㅣㅐ ㅈㅐㄱㅣㅇ!" * 1000000
        self.assertEqual(convert_key(input_text, "ko", False), expected)


if __name__ == "__main__":
    unittest.main()

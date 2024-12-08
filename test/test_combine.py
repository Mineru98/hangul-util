import unittest

from hangul_utils.combine import combine, combine_by_code, combine_hangul


class TestCombineByCode(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(combine_by_code(), "가")

    def test_invalid_value(self):
        self.assertEqual(combine_by_code(-1, -1, -1), "")

    def test_ggeut(self):
        self.assertEqual(combine_by_code(1, 0, -1), "깋")


class TestCombine(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(combine(), "")

    def test_non_hangul(self):
        self.assertEqual(combine("a"), "a")

    def test_a(self):
        self.assertEqual(combine("ㅇ", "ㅏ"), "아")

    def test_an(self):
        self.assertEqual(combine("ㅇ", "ㅏ", "ㄴ"), "안")

    def test_bwelg(self):
        self.assertEqual(combine("ㅂ", "ㅞ", "ㄺ"), "뷁")
        self.assertEqual(combine("ㅂ", "ㅜㅔ", "ㄹㄱ"), "뷁")


class TestCombineHangul(unittest.TestCase):
    def test_ganada(self):
        self.assertEqual(combine_hangul("ㄱㅏㄴㅏㄷㅏ"), "가나다")

    def test_gannada(self):
        self.assertEqual(combine_hangul("ㄱㅏㄴㄴㅏㄷㅏ"), "간나다")

    def test_gapsada(self):
        self.assertEqual(combine_hangul("ㄱㅏㅂㅅㄴㅏㄷㅏ"), "값나다")

    def test_gapsnada(self):
        self.assertEqual(combine_hangul("ㄱㅏㅂㅅㄴㄴㅏㄷㅏ"), "값ㄴ나다")

    def test_gapssnada(self):
        self.assertEqual(combine_hangul("ㄱㅏㅂㅅㅅㄴㄴㅏㄷㅏ"), "값ㅅㄴ나다")

    def test_gapsasnada(self):
        self.assertEqual(combine_hangul("ㄱㅏㅂㅅㅏㅏㅅㄴㄴㅏㄷㅏ"), "갑사ㅏㅅㄴ나다")

    def test_gapsasannada(self):
        self.assertEqual(combine_hangul("ㄱㅏㅂㅅㅏㅅㅏㄴㄴㅏㄷㅏ"), "갑사산나다")

    def test_gapsatnada(self):
        self.assertEqual(combine_hangul("ㄱㅏㅂㅅㅏㅅㄴㄴㅏㄷㅏ"), "갑삿ㄴ나다")

    def test_gapsatnwaeda(self):
        self.assertEqual(combine_hangul("ㄱㅏㅂㅅㅏㅅㄴㄴㅜㅔㄷㅏ"), "갑삿ㄴ눼다")

    def test_subak(self):
        self.assertEqual(combine_hangul("ㅅㅜㅂㅏㄱ"), "수박")

    def test_special_case1(self):
        self.assertEqual(combine_hangul("ㅗㄷㅣㅣㅐ ㅂㅏㅂㅗㅇ!"), "ㅗ디ㅣㅐ 바봉!")

    def test_special_case2(self):
        self.assertEqual(
            combine_hangul("ㅗㄷㅣㅓㅕㅜㅠㅣㅐ ㅂㅏㅂㅗㅇ!"), "ㅗ디ㅓㅕㅜㅠㅣㅐ 바봉!"
        )

    def test_special_case3(self):
        self.assertEqual(
            combine_hangul("ㅗㄷㅣㅓㅇㅅㅎㅇㅇㅇㅇㅕㅜㅠㅣㅐ ㅂㅏㅂㅗㅇ!"),
            "ㅗ디ㅓㅇㅅㅎㅇㅇㅇ여ㅜㅠㅣㅐ 바봉!",
        )

    def test_empty(self):
        self.assertEqual(combine_hangul(), "")

    def test_non_hangul(self):
        self.assertEqual(combine_hangul("Ab!6k+@_ @"), "Ab!6k+@_ @")

    def test_annyeonghaseyo(self):
        self.assertEqual(combine_hangul(["ㅇㅏㄴㄴㅕㅇㅎㅏㅅㅔㅇㅛ"]), "안녕하세요")
        self.assertEqual(combine_hangul("ㅇㅏㄴㄴㅕㅇㅎㅏㅅㅔㅇㅛ"), "안녕하세요")
        self.assertEqual(
            combine_hangul([["ㅇㅏㄴㅈ"], ["ㄴㅕㅇㅎㅏㅅㅔㅇㅛ"]]), "앉녕하세요"
        )
        self.assertEqual(
            combine_hangul([["ㅇㅏㄴ"], ["ㅈㄴㅕㅇㅎㅏㅅㅔㅇㅛ"]]), "안ㅈ녕하세요"
        )

    def test_all_cases(self):
        self.assertEqual(
            combine_hangul(
                [
                    ["ㅂㅜ", "ㅔ", "ㄹㄱ"],
                    "ㅅ",
                    "ㅗ",
                    "ㅐ",
                    "ㄹ",
                    "ㅁ",
                    ["ㅎㅜㅔㅂㅅ"],
                    "ㄱ",
                    ["ㅏ", "ㅅ", "ㅏ"],
                ]
            ),
            "뷁쇎휎ㄱㅏ사",
        )

    def test_timeout(self):
        input_str = "ㄱㅏㅂㅅ" * 1000000
        expected = "값" * 1000000
        self.assertEqual(combine_hangul(input_str), expected)


if __name__ == "__main__":
    unittest.main()

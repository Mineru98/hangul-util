import unittest

from hangul_utils.divide import divide, divide_hangul, divide_hangul_by_groups


class TestDivide(unittest.TestCase):
    def test_non_hangul(self):
        self.assertEqual(divide("a"), ["a"])

    def test_han(self):
        self.assertEqual(divide("한"), ["ㅎ", "ㅏ", "ㄴ"])

    def test_han_object(self):
        self.assertEqual(
            divide("한", result_type="dict"),
            {"cho": "ㅎ", "jung": "ㅏ", "jong": "ㄴ"},
        )

    def test_han_string(self):
        self.assertEqual(divide("한", result_type="str"), "ㅎㅏㄴ")

    def test_bbang(self):
        self.assertEqual(divide("빵"), ["ㅃ", "ㅏ", "ㅇ"])

    def test_byeolg(self):
        self.assertEqual(divide("뷁", is_split=True), ["ㅂ", "ㅜ", "ㅔ", "ㄹ", "ㄱ"])
        self.assertEqual(divide("뷁", is_split=False), ["ㅂ", "ㅞ", "ㄺ"])


class TestDivideHangulByGroups(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(divide_hangul_by_groups(""), [])

    def test_annyeong_haseyo(self):
        self.assertEqual(
            divide_hangul_by_groups("안녕하세요"),
            [
                ["ㅇ", "ㅏ", "ㄴ"],
                ["ㄴ", "ㅕ", "ㅇ"],
                ["ㅎ", "ㅏ"],
                ["ㅅ", "ㅔ"],
                ["ㅇ", "ㅛ"],
            ],
        )

    def test_hello_annyeong(self):
        self.assertEqual(
            divide_hangul_by_groups("Hello, 안녕하세요"),
            [
                ["H"],
                ["e"],
                ["l"],
                ["l"],
                ["o"],
                [","],
                [" "],
                ["ㅇ", "ㅏ", "ㄴ"],
                ["ㄴ", "ㅕ", "ㅇ"],
                ["ㅎ", "ㅏ"],
                ["ㅅ", "ㅔ"],
                ["ㅇ", "ㅛ"],
            ],
        )

    def test_complex_chars(self):
        self.assertEqual(
            divide_hangul_by_groups("값뷁ㅅ쇏"),
            [
                ["ㄱ", "ㅏ", "ㅂ", "ㅅ"],
                ["ㅂ", "ㅜ", "ㅔ", "ㄹ", "ㄱ"],
                ["ㅅ"],
                ["ㅅ", "ㅗ", "ㅐ", "ㄹ", "ㅂ"],
            ],
        )
        self.assertEqual(
            divide_hangul_by_groups("값뷁ㅅ쇏", is_split=False),
            [["ㄱ", "ㅏ", "ㅄ"], ["ㅂ", "ㅞ", "ㄺ"], ["ㅅ"], ["ㅅ", "ㅙ", "ㄼ"]],
        )


class TestDivideHangul(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(divide_hangul(""), [])

    def test_annyeong_haseyo(self):
        self.assertEqual(
            divide_hangul("안녕하세요"),
            ["ㅇ", "ㅏ", "ㄴ", "ㄴ", "ㅕ", "ㅇ", "ㅎ", "ㅏ", "ㅅ", "ㅔ", "ㅇ", "ㅛ"],
        )

    def test_hello_annyeong(self):
        self.assertEqual(
            divide_hangul("Hello, 안녕하세요"),
            [
                "H",
                "e",
                "l",
                "l",
                "o",
                ",",
                " ",
                "ㅇ",
                "ㅏ",
                "ㄴ",
                "ㄴ",
                "ㅕ",
                "ㅇ",
                "ㅎ",
                "ㅏ",
                "ㅅ",
                "ㅔ",
                "ㅇ",
                "ㅛ",
            ],
        )

    def test_complex_chars(self):
        self.assertEqual(
            divide_hangul("값뷁쇏"),
            [
                "ㄱ",
                "ㅏ",
                "ㅂ",
                "ㅅ",
                "ㅂ",
                "ㅜ",
                "ㅔ",
                "ㄹ",
                "ㄱ",
                "ㅅ",
                "ㅗ",
                "ㅐ",
                "ㄹ",
                "ㅂ",
            ],
        )
        self.assertEqual(
            divide_hangul("값뷁쇏", is_split=False),
            ["ㄱ", "ㅏ", "ㅄ", "ㅂ", "ㅞ", "ㄺ", "ㅅ", "ㅙ", "ㄼ"],
        )

    def test_timeout(self):
        input_str = "값쉛" * 100000
        result = list("ㄱㅏㅂㅅㅅㅜㅔㄹㅂ" * 100000)
        self.assertEqual(divide_hangul(input_str), result)


if __name__ == "__main__":
    unittest.main()

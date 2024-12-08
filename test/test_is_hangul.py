import unittest

from hangul_utils.is_hangul import is_hangul, is_hangul_by_code, is_hangul_by_groups


class TestIsHangul(unittest.TestCase):
    def test_is_hangul_by_code(self):
        # 조합된 한글 값
        self.assertTrue(is_hangul_by_code(ord("아")))
        self.assertTrue(is_hangul_by_code(ord("뷁")))

        # 조합된 한글 아닌 값
        self.assertFalse(is_hangul_by_code(ord("1")))
        self.assertFalse(is_hangul_by_code(ord("s")))
        self.assertFalse(is_hangul_by_code(ord("@")))
        self.assertFalse(is_hangul_by_code(ord("ㄱ")))
        self.assertFalse(is_hangul_by_code(ord("ㅏ")))

    def test_is_hangul(self):
        # 한글 값
        self.assertTrue(is_hangul("자"))
        self.assertTrue(is_hangul("안녕하세요"))
        self.assertTrue(is_hangul("자바스크립트"))

        # 한글 아닌 값 포함
        self.assertFalse(is_hangul("Hello, world!"))
        self.assertFalse(is_hangul("12345"))
        self.assertFalse(is_hangul("안녕하세요, Hello, world!"))
        self.assertFalse(is_hangul("Hello! 안녕!"))

        # 시간초과 테스트
        input_str = "값" * 1000000
        self.assertTrue(is_hangul(input_str))

    def test_is_hangul_by_groups(self):
        # 안녕하세요
        self.assertEqual(
            is_hangul_by_groups("안녕하세요"), [True, True, True, True, True]
        )

        # 자바스크립트.
        self.assertEqual(
            is_hangul_by_groups("자바스크립트."),
            [True, True, True, True, True, True, False],
        )

        # Hello, 안녕!
        self.assertEqual(
            is_hangul_by_groups("Hello, 안녕!"),
            [False, False, False, False, False, False, False, True, True, False],
        )

        # 시간초과 테스트
        input_str = "값" * 1000000
        expected = [True] * 1000000
        self.assertEqual(is_hangul_by_groups(input_str), expected)


if __name__ == "__main__":
    unittest.main()

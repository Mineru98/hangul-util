import unittest

from hangul_utils.is_jung import is_jung, is_jung_by_code, is_jung_by_groups


class TestJung(unittest.TestCase):
    def test_is_jung_by_code(self):
        self.assertTrue(is_jung_by_code(ord("ㅏ")))
        self.assertFalse(is_jung_by_code(ord("ㄱ")))
        self.assertFalse(is_jung_by_code(ord("a")))

    def test_is_jung(self):
        self.assertTrue(is_jung("ㅏㅣㅜ"))
        self.assertFalse(is_jung("ㅏㄱㅣ"))
        self.assertFalse(is_jung(""))

        # 시간초과 테스트
        input_str = "ㅜ" * 1000000
        self.assertTrue(is_jung(input_str))

    def test_is_jung_by_groups(self):
        self.assertEqual(is_jung_by_groups("ㅏㅣㅜ"), [True, True, True])
        self.assertEqual(is_jung_by_groups("ㅏㄱㅣ"), [True, False, True])
        self.assertEqual(is_jung_by_groups(""), [])

        # 시간초과 테스트
        input_str = "ㅏ" * 1000000
        result = [True] * 1000000
        self.assertEqual(is_jung_by_groups(input_str), result)


if __name__ == "__main__":
    unittest.main()

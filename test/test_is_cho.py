import unittest

from hangul_utils.is_cho import is_cho, is_cho_by_char, is_cho_by_groups


class TestCho(unittest.TestCase):
    def test_is_cho_by_char(self):
        self.assertTrue(is_cho_by_char("ㄱ"))
        self.assertTrue(is_cho_by_char("ㄴ"))
        self.assertTrue(is_cho_by_char("ㅎ"))
        self.assertFalse(is_cho_by_char("ㅏ"))
        self.assertFalse(is_cho_by_char("ㅓ"))
        self.assertFalse(is_cho_by_char("야"))

    def test_is_cho(self):
        self.assertFalse(is_cho(""))
        self.assertTrue(is_cho("ㄱㅎㄴ"))
        self.assertTrue(is_cho("ㅎㅎㅎ"))
        self.assertFalse(is_cho("ㅎㄴa"))
        self.assertFalse(is_cho("hello"))

        # 시간초과 테스트
        input_str = "ㄱ" * 1000000
        self.assertTrue(is_cho(input_str))

    def test_is_cho_by_groups(self):
        self.assertEqual(is_cho_by_groups(""), [])
        self.assertEqual(is_cho_by_groups("ㄱㅎㄴ"), [True, True, True])
        self.assertEqual(is_cho_by_groups("ㅎㄴa"), [True, True, False])
        self.assertEqual(is_cho_by_groups("ㅎㅏㄾㅆ"), [True, False, False, True])

        # 시간초과 테스트
        input_str = "ㄱ" * 1000000
        result = [True] * 1000000
        self.assertEqual(is_cho_by_groups(input_str), result)


if __name__ == "__main__":
    unittest.main()

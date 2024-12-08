import unittest

from hangul_utils.is_jong import is_jong, is_jong_by_code, is_jong_by_groups


class TestJong(unittest.TestCase):
    def test_is_jong_by_code(self):
        self.assertTrue(is_jong_by_code(12593))  # "ㄱ"
        self.assertTrue(is_jong_by_code(12622))  # "ㅊ"
        self.assertTrue(is_jong_by_code(12595))  # "ㅊ"
        self.assertFalse(is_jong_by_code(44032))  # "가"
        self.assertFalse(is_jong_by_code(97))  # "a"

    def test_is_jong(self):
        self.assertFalse(is_jong(""))
        self.assertTrue(is_jong("ㄳㅂㄷㅈ"))
        self.assertFalse(is_jong("ㄳㅂ2ㄷㅈ"))
        self.assertFalse(is_jong("가나다라"))
        self.assertFalse(is_jong("ㄱㅏㄷㅏ"))

        # 시간초과 테스트
        input_str = "ㅂ" * 1000000
        self.assertTrue(is_jong(input_str))

    def test_is_jong_by_groups(self):
        self.assertEqual(is_jong_by_groups("ㄱㅂㄷㅈ"), [True, True, True, True])
        self.assertEqual(is_jong_by_groups("가나다라"), [False, False, False, False])
        self.assertEqual(is_jong_by_groups("ㄳㅏㄷㅏ"), [True, False, True, False])

        # 시간초과 테스트
        input_str = "ㄳ" * 1000000
        result = [True] * 1000000
        self.assertEqual(is_jong_by_groups(input_str), result)


if __name__ == "__main__":
    unittest.main()

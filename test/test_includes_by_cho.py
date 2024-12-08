import re
import unittest

from hangul_utils.includes_by_cho import includes_by_cho, make_regex_by_cho


class TestIncludesByCho(unittest.TestCase):
    def test_make_regex_by_cho_with_mixed(self):
        search = "ㄱ나다라마바ㅅ"
        self.assertEqual(
            make_regex_by_cho(search), re.compile("([가-깋]나다라마바[사-싷])")
        )

    def test_make_regex_by_cho_with_cho(self):
        search = "ㄱㄱ"
        self.assertEqual(make_regex_by_cho(search), re.compile("([가-깋][가-깋])"))

    def test_includes_by_cho_single_match(self):
        search = "ㄱ"
        word = "가나다라마바사"
        self.assertTrue(includes_by_cho(search, word))

    def test_includes_by_cho_no_match(self):
        search = "ㅇ"
        word = "가나다라마바사"
        self.assertFalse(includes_by_cho(search, word))

    def test_includes_by_cho_consecutive_match(self):
        search = "ㄷㄹ"
        word = "가나다라마바사"
        self.assertTrue(includes_by_cho(search, word))

    def test_includes_by_cho_consecutive_no_match(self):
        search = "ㄱㄹ"
        word = "가나다라마바사"
        self.assertFalse(includes_by_cho(search, word))

    def test_includes_by_cho_mixed_pattern(self):
        search = "가ㄴㄷ라"
        word = "가나다라마바사"
        self.assertTrue(includes_by_cho(search, word))


if __name__ == "__main__":
    unittest.main()

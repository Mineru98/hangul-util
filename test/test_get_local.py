import unittest

from hangul_utils.get_local import get_local, get_local_by_groups


class TestGetLocal(unittest.TestCase):
    def test_korean(self):
        self.assertEqual(get_local("안녕하세요"), "ko")

    def test_english(self):
        self.assertEqual(get_local("Hello world"), "en")

    def test_number(self):
        self.assertEqual(get_local("1234"), "number")

    def test_special(self):
        self.assertEqual(get_local("!@#$%^&*()_+"), "special")

    def test_etc(self):
        self.assertEqual(get_local("こんにちは！!123"), "etc")


class TestGetLocalByGroups(unittest.TestCase):
    def test_korean_groups(self):
        self.assertEqual(
            get_local_by_groups("안녕하세요"), ["ko", "ko", "ko", "ko", "ko"]
        )

    def test_english_groups(self):
        self.assertEqual(
            get_local_by_groups("Hello, world!"),
            [
                "en",
                "en",
                "en",
                "en",
                "en",
                "special",
                "special",
                "en",
                "en",
                "en",
                "en",
                "en",
                "special",
            ],
        )

    def test_number_groups(self):
        self.assertEqual(
            get_local_by_groups("1234"), ["number", "number", "number", "number"]
        )

    def test_special_groups(self):
        self.assertEqual(get_local_by_groups("!@#$%^&*()_+"), ["special"] * 12)

    def test_mixed_groups(self):
        self.assertEqual(
            get_local_by_groups("こんにちは!123"),
            [
                "etc",
                "etc",
                "etc",
                "etc",
                "etc",
                "special",
                "number",
                "number",
                "number",
            ],
        )

    def test_percentage(self):
        result = get_local_by_groups(
            "안녕하세요! Hello, world! 1234 #", is_percent=True
        )
        self.assertEqual(
            result,
            {"ko": 18.52, "en": 37.04, "number": 14.81, "special": 29.63, "etc": 0},
        )

    def test_special_percentage(self):
        result = get_local_by_groups("!@#$%^&*()_+", is_percent=True)
        self.assertEqual(
            result, {"ko": 0, "en": 0, "number": 0, "special": 100, "etc": 0}
        )

    def test_performance(self):
        word = "안녕하세요! Hello, world! 1234 #" * 1000000
        result = get_local_by_groups(word, is_percent=True)
        self.assertEqual(
            result,
            {"ko": 18.52, "en": 37.04, "number": 14.81, "special": 29.63, "etc": 0},
        )


if __name__ == "__main__":
    unittest.main()

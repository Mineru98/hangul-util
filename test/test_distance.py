import unittest

from hangul_utils.distance import correct_by_distance, get_distance


class TestDistance(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(get_distance("파인애플", ""), 4)
        self.assertEqual(get_distance("", "파인애플"), 4)
        self.assertEqual(get_distance("", ""), 0)

    def test_pineapple(self):
        self.assertEqual(get_distance("파인애플", "파일해플"), 2)

    def test_performance(self):
        input1 = "팝" * 10000
        input2 = "핍" * 10000
        self.assertEqual(get_distance(input1, input2), 10000)


class TestCorrectByDistance(unittest.TestCase):
    def setUp(self):
        self.word_list = [
            "사자",
            "무과",
            "사과파이",
            "파인애플",
            "망고",
            "변호사",
            "사고",
            "사과",
            "귤",
            "토끼",
            "코끼리",
        ]

    def test_apple(self):
        self.assertEqual(
            correct_by_distance("사과", self.word_list),
            ["사과", "사고", "사자", "무과"],
        )

        self.assertEqual(
            correct_by_distance("사과", self.word_list, is_split=False),
            ["사과", "사자", "무과", "사고", "사과파이", "망고", "귤", "토끼"],
        )

    def test_performance(self):
        input_text = "팝" * 1000
        input_list = ["핍" * 1000, "쉽" * 1000] * 1000
        self.assertEqual(correct_by_distance(input_text, input_list), [])


if __name__ == "__main__":
    unittest.main()

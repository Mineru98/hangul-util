import unittest

from hangul_utils.normalize import normalize


class TestNormalize(unittest.TestCase):
    def test_normalize_sagwa(self):
        self.assertEqual(normalize("사과"), "sa gwa")

    def test_normalize_italia(self):
        self.assertEqual(normalize("이탈리아"), "i tar ri a")
        self.assertEqual(normalize("이탈리아", False), "itarria")

    def test_normalize_other(self):
        self.assertEqual(normalize("그 외"), "geu oe")

    def test_normalize_mixed(self):
        self.assertEqual(normalize("사과! 그리고 sagwa!"), "sa gwa ! geu ri go sagwa!")
        self.assertEqual(
            normalize("사과! 그리고 sagwa!", False), "sagwa! geurigo sagwa!"
        )

    def test_normalize_performance(self):
        input_str = "사과! 그리고 sagwa!" * 100000
        result = "sa gwa ! geu ri go sagwa!" * 100000
        self.assertEqual(normalize(input_str), result)


if __name__ == "__main__":
    unittest.main()

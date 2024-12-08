import unittest

from hangul_utils.josa import format_josa, josa


class TestJosa(unittest.TestCase):
    def test_josa(self):
        self.assertEqual(josa("영희", "는"), "는")

    def test_format_josa(self):
        self.assertEqual(
            format_josa("I have an apple[은/는]"), "I have an apple[은/는]"
        )
        self.assertEqual(format_josa("[은/는]"), "[은/는]")
        self.assertEqual(format_josa("영희[은/는]"), "영희는")
        self.assertEqual(format_josa("인생[이란/란]"), "인생이란")
        self.assertEqual(format_josa("인생[란/테스트]"), "인생이란")


if __name__ == "__main__":
    unittest.main()

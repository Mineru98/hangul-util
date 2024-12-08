import unittest

from hangul_utils.utils import (
    chunk_at_end,
    get_nested_property,
    is_number,
    make_percent_by_object,
    reverse_by_array,
    reverse_by_object,
    split_by_key,
    zero_pad,
)


class TestUtils(unittest.TestCase):
    def test_is_number_non_numbers(self):
        self.assertFalse(is_number(""))
        self.assertFalse(is_number(None))
        self.assertFalse(is_number("abc"))
        self.assertFalse(is_number("test"))
        self.assertFalse(is_number("100,000.123"))
        self.assertFalse(is_number(True))
        self.assertFalse(is_number(False))
        self.assertFalse(is_number([]))
        self.assertFalse(is_number({}))

    def test_is_number_numbers(self):
        self.assertTrue(is_number(0))
        self.assertTrue(is_number(123))
        self.assertTrue(is_number(-123))
        self.assertTrue(is_number(0.123))
        self.assertTrue(is_number(123.213))

    def test_split_by_key(self):
        self.assertEqual(split_by_key(""), [])
        self.assertEqual(split_by_key("[0].a"), ["0", "a"])
        self.assertEqual(split_by_key("name.detail"), ["name", "detail"])

    def test_zero_pad(self):
        self.assertEqual(zero_pad(5, 2), "05")
        self.assertEqual(zero_pad("test", 10), "000000test")
        self.assertEqual(zero_pad("test", 10, "-"), "------test")
        self.assertEqual(zero_pad(123, 5), "00123")
        self.assertEqual(zero_pad("", 3), "000")

    def test_chunk_at_end(self):
        self.assertEqual(chunk_at_end("abcdefg", 2), ["fg", "de", "bc", "a"])
        self.assertEqual(chunk_at_end("abcdefg", 4), ["defg", "abc"])

        self.assertEqual(chunk_at_end("abc"), ["c", "b", "a"])
        self.assertEqual(chunk_at_end("abc", 3), ["abc"])

        self.assertEqual(chunk_at_end("00000001", 4), ["0001", "0000"])
        self.assertEqual(chunk_at_end("00000001", 2), ["01", "00", "00", "00"])

        self.assertEqual(chunk_at_end(""), [])

        # 시간초과 테스트
        input_str = "0101" * 400000
        result = list("1010" * 400000)
        self.assertEqual(chunk_at_end(input_str, 1), result)

    def test_make_percent_by_object(self):
        self.assertEqual(make_percent_by_object({}), {})

        self.assertEqual(
            make_percent_by_object({"a": 10, "b": 20, "c": 30}),
            {"a": 16.67, "b": 33.33, "c": 50},
        )

        self.assertEqual(make_percent_by_object({"a": 0, "b": 10}), {"a": 0, "b": 100})

    def test_reverse_by_object(self):
        self.assertEqual(
            reverse_by_object({"a": 1, "b": 2, "c": 3}), {"1": "a", "2": "b", "3": "c"}
        )
        self.assertEqual(
            reverse_by_object({"1": "a", "2": "b", "3": "c"}),
            {"a": "1", "b": "2", "c": "3"},
        )
        self.assertEqual(
            reverse_by_object(["a", "b", "c"]), {"a": "0", "b": "1", "c": "2"}
        )

    def test_reverse_by_array(self):
        self.assertEqual(
            reverse_by_array(
                [[["습니다"], ["다", "어", "음"]], [["입니다"], ["이다"]]]
            ),
            [[["이다"], ["입니다"]], [["음", "어", "다"], ["습니다"]]],
        )

        self.assertEqual(
            reverse_by_array([1, 2, 3, [4, [5, 6, 7]]]), [[[7, 6, 5], 4], 3, 2, 1]
        )


if __name__ == "__main__":
    unittest.main()

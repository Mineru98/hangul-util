import unittest

from hangul_utils.encode import decode, encode


class TestEncode(unittest.TestCase):
    def test_string(self):
        """문자열 인코딩/디코딩 테스트"""
        self.assertEqual(decode(encode("구오")), "구오")

    def test_mixed_string(self):
        """혼합 문자열 인코딩/디코딩 테스트"""
        self.assertEqual(decode(encode("감!사3합$니다.")), "감!사3합$니다.")

    def test_array(self):
        """배열 인코딩/디코딩 테스트"""
        self.assertEqual(decode(encode([1, 2, 3])), [1, 2, 3])

    def test_dict(self):
        """딕셔너리 인코딩/디코딩 테스트"""
        self.assertEqual(decode(encode({"a": 1, "b": 2})), {"a": 1, "b": 2})

    def test_mixed_objects(self):
        """혼합 객체 인코딩/디코딩 테스트"""
        input_data = [{"a": 1, "b": 2}, {"a": 1, "b": 2}]
        self.assertEqual(decode(encode(input_data)), input_data)

    def test_timeout(self):
        """대용량 데이터 시간초과 테스트"""
        input_data = "감!사3합$니다." * 40000
        self.assertEqual(decode(encode(input_data)), input_data)


if __name__ == "__main__":
    unittest.main()

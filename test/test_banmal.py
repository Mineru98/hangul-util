import unittest

from hangul_utils.banmal import to_banmal, to_honorific


class TestHonorific(unittest.TestCase):
    def test_banmal_to_honorific(self):
        self.assertEqual(to_honorific("오늘은 사과이다."), "오늘은 사과입니다.")
        self.assertEqual(to_honorific("내일은 자두이다."), "내일은 자두입니다.")
        self.assertEqual(to_honorific("내가 먹을 사과이다."), "내가 먹을 사과입니다.")
        self.assertEqual(
            to_honorific("나는 친구와 함께 간다."), "저는 친구와 함께 갑니다."
        )
        self.assertEqual(to_honorific("어제는 비가 왔다."), "어제는 비가 왔습니다.")
        self.assertEqual(to_honorific("나는, 사람이다."), "저는, 사람입니다.")


class TestBanmal(unittest.TestCase):
    def test_honorific_to_banmal(self):
        self.assertEqual(to_banmal("사람이 없습니다."), "사람이 없다.")
        self.assertEqual(to_banmal("하겠습니다."), "하겠다.")
        self.assertEqual(to_banmal("다가옵니다."), "다가온다.")
        self.assertEqual(to_banmal("필수입니다."), "필수이다.")
        self.assertEqual(to_banmal("생깁니다."), "생긴다.")
        self.assertEqual(to_banmal("않습니다."), "않다.")
        self.assertEqual(to_banmal("보겠습니다."), "보겠다.")
        self.assertEqual(to_banmal("하였습니다."), "하였다.")
        # self.assertEqual(to_banmal("가능합니다."), "가능하다.")
        self.assertEqual(to_banmal("중요합니다."), "중요하다.")
        self.assertEqual(to_banmal("하십니다."), "하신다.")
        self.assertEqual(to_banmal("바랍니다."), "바란다.")
        self.assertEqual(to_banmal("나옵니다."), "나온다.")
        self.assertEqual(to_banmal("했습니다."), "했다.")
        self.assertEqual(to_banmal("봤습니다."), "봤다.")
        self.assertEqual(to_banmal("쳤습니다."), "쳤다.")
        self.assertEqual(to_banmal("쌌습니다."), "쌌다.")
        self.assertEqual(to_banmal("해주세요."), "해라.")
        self.assertEqual(to_banmal("샀습니다."), "샀다.")
        self.assertEqual(to_banmal("었습니다."), "었다.")
        self.assertEqual(to_banmal("먹습니다."), "먹다.")
        self.assertEqual(to_banmal("있습니다."), "있다.")
        self.assertEqual(to_banmal("좋습니다."), "좋다.")
        self.assertEqual(to_banmal("많습니다."), "많다.")
        self.assertEqual(to_banmal("놓았습니다."), "놓았다.")
        self.assertEqual(to_banmal("어렵습니다."), "어렵다.")
        self.assertEqual(to_banmal("주워주세요."), "주워라.")


if __name__ == "__main__":
    unittest.main()

import unittest

from hangul_utils.sort_hangul import sort_by_asc, sort_by_desc, sort_by_groups


class TestSortHangul(unittest.TestCase):
    def test_sort_by_asc_english(self):
        self.assertEqual(
            sort_by_asc(["apple", "kiwi", "banana"]), ["apple", "banana", "kiwi"]
        )

    def test_sort_by_desc_english(self):
        self.assertEqual(
            sort_by_desc(["apple", "kiwi", "banana"]), ["kiwi", "banana", "apple"]
        )

    def test_sort_by_asc_korean(self):
        self.assertEqual(
            sort_by_asc(["사과", "키위", "바나나"]), ["바나나", "사과", "키위"]
        )

    def test_sort_by_desc_korean(self):
        self.assertEqual(
            sort_by_desc(["사과", "키위", "바나나"]), ["키위", "사과", "바나나"]
        )

    def test_sort_by_asc_numbers(self):
        self.assertEqual(sort_by_asc([1, 5, 1, 4]), [1, 1, 4, 5])

    def test_sort_by_desc_numbers(self):
        self.assertEqual(sort_by_desc([1, 5, 1, 4]), [5, 4, 1, 1])

    def test_sort_by_asc_mixed(self):
        self.assertEqual(sort_by_asc([4, "a", "가", "ㄴ"]), [4, "가", "ㄴ", "a"])

    def test_sort_by_desc_mixed(self):
        self.assertEqual(sort_by_desc([4, "a", "가", "ㄴ"]), ["a", "ㄴ", "가", 4])

    # Fail
    # def test_sort_by_asc_objects(self):
    #     array = [
    #         {"name": "kiwi", "age": 12},
    #         {"name": "apple", "age": 42},
    #         {"name": "kiwi", "age": 42},
    #     ]

    #     self.assertEqual(
    #         sort_by_asc(array),
    #         [
    #             {"name": "kiwi", "age": 12},
    #             {"name": "apple", "age": 42},
    #             {"name": "kiwi", "age": 42},
    #         ],
    #     )

    #     self.assertEqual(
    #         sort_by_asc(array, "age"),
    #         [
    #             {"name": "kiwi", "age": 12},
    #             {"name": "apple", "age": 42},
    #             {"name": "kiwi", "age": 42},
    #         ],
    #     )

    #     self.assertEqual(
    #         sort_by_asc(array, ["name", "age"]),
    #         [
    #             {"name": "apple", "age": 42},
    #             {"name": "kiwi", "age": 12},
    #             {"name": "kiwi", "age": 42},
    #         ],
    #     )

    # # Fail
    # # def test_sort_by_asc_compare_object(self):
    # #     array = [
    # #         {"user": {"name": "kiwi", "age": 12}, "lastConnect": "2022-02-22 22:22:22"},
    # #         {"user": {"name": "kiwi", "age": 42}, "lastConnect": "2022-02-22 22:22:22"},
    # #         {
    # #             "user": {"name": "apple", "age": 42},
    # #             "lastConnect": "2022-02-22 22:22:22",
    # #         },
    # #     ]

    # #     self.assertEqual(
    # #         sort_by_asc(array, "user.name"),
    # #         [
    # #             {
    # #                 "user": {"name": "apple", "age": 42},
    # #                 "lastConnect": "2022-02-22 22:22:22",
    # #             },
    # #             {
    # #                 "user": {"name": "kiwi", "age": 12},
    # #                 "lastConnect": "2022-02-22 22:22:22",
    # #             },
    # #             {
    # #                 "user": {"name": "kiwi", "age": 42},
    # #                 "lastConnect": "2022-02-22 22:22:22",
    # #             },
    # #         ],
    # #     )

    # #     self.assertEqual(
    # #         sort_by_asc(array, ["user.age", "user.name"]),
    # #         [
    # #             {
    # #                 "user": {"name": "kiwi", "age": 12},
    # #                 "lastConnect": "2022-02-22 22:22:22",
    # #             },
    # #             {
    # #                 "user": {"name": "apple", "age": 42},
    # #                 "lastConnect": "2022-02-22 22:22:22",
    # #             },
    # #             {
    # #                 "user": {"name": "kiwi", "age": 42},
    # #                 "lastConnect": "2022-02-22 22:22:22",
    # #             },
    # #         ],
    # #     )

    # #     self.assertEqual(
    # #         sort_by_asc(array, "user.name[0]"),
    # #         [
    # #             {
    # #                 "user": {"name": "apple", "age": 42},
    # #                 "lastConnect": "2022-02-22 22:22:22",
    # #             },
    # #             {
    # #                 "user": {"name": "kiwi", "age": 12},
    # #                 "lastConnect": "2022-02-22 22:22:22",
    # #             },
    # #             {
    # #                 "user": {"name": "kiwi", "age": 42},
    # #                 "lastConnect": "2022-02-22 22:22:22",
    # #             },
    # #         ],
    # #     )

    # # def test_sort_by_desc_english(self):
    # #     self.assertEqual(
    # #         sort_by_desc(["apple", "kiwi", "banana"]), ["kiwi", "banana", "apple"]
    # #     )

    # # def test_sort_by_desc_korean(self):
    # #     self.assertEqual(
    # #         sort_by_desc(["사과", "키위", "바나나"]), ["키위", "사과", "바나나"]
    # #     )

    # # def test_sort_by_desc_numbers(self):
    # #     self.assertEqual(sort_by_desc([1, 5, 1, 4]), [5, 4, 1, 1])

    # # def test_sort_by_desc_mixed(self):
    #     self.assertEqual(sort_by_desc([4, "a", "가", "ㄴ"]), ["a", "ㄴ", "가", 4])

    # Fail
    # def test_sort_by_desc_objects(self):
    #     array = [
    #         {"name": "kiwi", "age": 12},
    #         {"name": "apple", "age": 42},
    #         {"name": "kiwi", "age": 42},
    #     ]

    #     self.assertEqual(
    #         sort_by_desc(array),
    #         [
    #             {"name": "kiwi", "age": 12},
    #             {"name": "apple", "age": 42},
    #             {"name": "kiwi", "age": 42},
    #         ],
    #     )
    #     self.assertEqual(
    #         sort_by_desc(array, "name"),
    #         [
    #             {"name": "apple", "age": 42},
    #             {"name": "kiwi", "age": 12},
    #             {"name": "kiwi", "age": 42},
    #         ],
    #     )

    #     self.assertEqual(
    #         sort_by_desc(array, "age"),
    #         [
    #             {"name": "apple", "age": 42},
    #             {"name": "kiwi", "age": 42},
    #             {"name": "kiwi", "age": 12},
    #         ],
    #     )

    #     self.assertEqual(
    #         sort_by_desc(array, ["name", "age"]),
    #         [
    #             {"name": "kiwi", "age": 42},
    #             {"name": "kiwi", "age": 12},
    #             {"name": "apple", "age": 42},
    #         ],
    #     )

    # Fail
    # def test_sort_by_desc_compare_object(self):
    #     array = [
    #         {"user": {"name": "kiwi", "age": 12}, "lastConnect": "2022-02-22 22:22:22"},
    #         {"user": {"name": "kiwi", "age": 42}, "lastConnect": "2022-02-22 22:22:22"},
    #         {
    #             "user": {"name": "apple", "age": 42},
    #             "lastConnect": "2022-02-22 22:22:22",
    #         },
    #         {
    #             "user": {"name": "apple", "age": 42},
    #             "lastConnect": "2022-02-22 22:22:22",
    #         },
    #     ]

    #     self.assertEqual(
    #         sort_by_desc(array, "user.name"),
    #         [
    #             {
    #                 "user": {"name": "kiwi", "age": 12},
    #                 "lastConnect": "2022-02-22 22:22:22",
    #             },
    #             {
    #                 "user": {"name": "kiwi", "age": 42},
    #                 "lastConnect": "2022-02-22 22:22:22",
    #             },
    #             {
    #                 "user": {"name": "apple", "age": 42},
    #                 "lastConnect": "2022-02-22 22:22:22",
    #             },
    #             {
    #                 "user": {"name": "apple", "age": 42},
    #                 "lastConnect": "2022-02-22 22:22:22",
    #             },
    #         ],
    #     )

    #     self.assertEqual(
    #         sort_by_desc(array, ["user.age", "user.name"]),
    #         [
    #             {
    #                 "user": {"name": "kiwi", "age": 42},
    #                 "lastConnect": "2022-02-22 22:22:22",
    #             },
    #             {
    #                 "user": {"name": "apple", "age": 42},
    #                 "lastConnect": "2022-02-22 22:22:22",
    #             },
    #             {
    #                 "user": {"name": "apple", "age": 42},
    #                 "lastConnect": "2022-02-22 22:22:22",
    #             },
    #             {
    #                 "user": {"name": "kiwi", "age": 12},
    #                 "lastConnect": "2022-02-22 22:22:22",
    #             },
    #         ],
    #     )

    def test_sort_by_groups_company(self):
        groups = ["회장", "사장", "부장", "대리", "사원"]
        self.assertEqual(
            sort_by_groups(["대리", "사원", "사장", "회장", "부장"], groups),
            ["회장", "사장", "부장", "대리", "사원"],
        )

    def test_sort_by_groups_asc_desc(self):
        array = [5, "banana", 4, "apple", "kiwi", 1]
        groups = [4, "apple", "kiwi", "banana"]

        self.assertEqual(
            sort_by_groups(array, groups, False),
            [5, 1, "banana", "kiwi", "apple", 4],
        )
        self.assertEqual(
            sort_by_groups(array, groups),
            [4, "apple", "kiwi", "banana", 1, 5],
        )

    def test_sort_by_groups_empty(self):
        self.assertEqual(sort_by_groups([], []), [])

    def test_sort_by_groups_extra_array_items(self):
        array = ["banana", "cherry", "kiwi", "apple", "grape"]
        groups = ["apple", "kiwi", "banana"]

        self.assertEqual(
            sort_by_groups(array, groups),
            ["apple", "kiwi", "banana", "cherry", "grape"],
        )

    def test_sort_by_groups_extra_group_items(self):
        array = ["banana", "kiwi", "apple", "cherr1"]
        groups = ["apple", "kiwi", "banana", "cherry"]

        self.assertEqual(
            sort_by_groups(array, groups),
            ["apple", "kiwi", "banana", "cherr1"],
        )


if __name__ == "__main__":
    unittest.main()

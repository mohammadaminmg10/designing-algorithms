import unittest

from game import is_valid_move, handle_bandits, calculate_gold, dynamic_collect_gold, greedy_collect_gold, \
    initialize_matrix


# add more complex unit tests and also the main matrix from the main project
class TestGoldCollection(unittest.TestCase):

    def setUp(self):
        self.matrix_1 = [
            [5, 'X', 3, '!'],
            [2, 0, 'X', 1],
            [4, 2, '!', 2],
            [0, 'X', 1, 5]
        ]
        self.matrix_2 = [
            ['X', 2, 'X', 4 ],
            [0  , 3,  1 ,'X'],
            [4  ,'X','!', 2 ],
            [1 ,  2, 'X',  5]
        ]
        self.matrix_3 = [
            [1, 2, 30],
            [4, '!', 6],
            [70, 8, 9]
        ]
        self.matrix_4 = [
            [0, 5, 'X', 2, 1],
            [4, '!', 3, 'X', 0],
            [3, '!', 'X', 1, 2],
            [1, 2, 3, 4, 5],
            ['X', 0, 1, '!', 3]
        ]
        self.matrix_5 = [
            ['!', 1, 2, 3],
            [4, 'X', 5, 6],
            [7, 8, 'X', 9],
            [10, 11, 12, 13]
        ]
        self.matrix_6 = [
            [2, 3, 'X', 1],
            ['!', 4, 5, 6],
            [7, 'X', 8, 9],
            [10, 11, 12, 'X']
        ]

    def test_initialize_matrix(self):
        matrix_input = [
            ['5', 'X', '3', '!'],
            ['2', '0', 'X', '1'],
            ['4', '2', '!', '2'],
            ['0', 'X', '1', '5']
        ]
        expected_output = [
            [5, 'X', 3, '!'],
            [2, 0, 'X', 1],
            [4, 2, '!', 2],
            [0, 'X', 1, 5]
        ]
        self.assertEqual(initialize_matrix(matrix_input), expected_output)

    def test_handle_bandits(self):
        self.assertEqual(handle_bandits(self.matrix_1, 0, 3, False), (0, True))
        self.assertEqual(handle_bandits(self.matrix_1, 2, 2, True), (0, False))
        self.assertEqual(handle_bandits(self.matrix_1, 0, 0, True), (-5, False))
        self.assertEqual(handle_bandits(self.matrix_1, 1, 0, False), (0, False))

    def test_is_valid_move(self):
        self.assertTrue(is_valid_move(self.matrix_1, 0, 0, -1, -1))
        self.assertFalse(is_valid_move(self.matrix_1, 0, 1, -1, -1))
        self.assertFalse(is_valid_move(self.matrix_1, 1, 2, 1, 2))
        self.assertTrue(is_valid_move(self.matrix_1, 1, 1, 0, 1))

    def test_calculate_gold(self):
        path = [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3)]
        self.assertEqual(calculate_gold(self.matrix_1, path), 17)
        path = [(0, 0), (0, 2), (1, 2), (2, 2), (2, 3), (3, 3)]
        self.assertEqual(calculate_gold(self.matrix_1, path), 11)

    def test_dynamic_collect_gold(self):
        expected_output_1 = (16, [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (3, 3)])
        expected_output_2 = (9, [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3), (3, 3)])
        expected_output_3 = (92, [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)])
        expected_output_4 = (25, [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 4)])
        expected_output_5 = (53, [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3)])
        expected_output_6 = (0, [])

        result_1 = dynamic_collect_gold(self.matrix_1)
        result_2 = dynamic_collect_gold(self.matrix_2)
        result_3 = dynamic_collect_gold(self.matrix_3)
        result_4 = dynamic_collect_gold(self.matrix_4)
        result_5 = dynamic_collect_gold(self.matrix_5)
        result_6 = dynamic_collect_gold(self.matrix_6)

        self.assertEqual(result_1, expected_output_1)
        self.assertEqual(result_2, expected_output_2)
        self.assertEqual(result_3, expected_output_3)
        self.assertEqual(result_4, expected_output_4)
        self.assertEqual(result_5, expected_output_5)
        self.assertEqual(result_6, expected_output_6)

    def test_greedy_collect_gold(self):
        self.assertEqual(greedy_collect_gold(self.matrix_1), (17, [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (3, 3)]))
        self.assertEqual(greedy_collect_gold(self.matrix_2), (9, [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3), (3, 3)]))
        self.assertEqual(greedy_collect_gold(self.matrix_3), (92, [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]))
        self.assertEqual(greedy_collect_gold(self.matrix_4), (22, [(0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4), (4, 4)]))
        self.assertEqual(greedy_collect_gold(self.matrix_5), (35, [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 3)]))
        self.assertEqual(greedy_collect_gold(self.matrix_6), (-1, []))


if __name__ == '__main__':
    unittest.main()

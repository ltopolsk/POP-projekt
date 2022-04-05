import unittest
import source.A_algorithm as A_algorithm
import source.naive_algorithm as naive_alogrithm
import numpy as np
import source.table as table


def is_acceptable(hidden_items):
    for item in hidden_items:
        for position in item.get_neighbors_pos():
            if not (None in position):
                for hidden in hidden_items:
                    if position == hidden.get_position():
                        return False
    return True


class AAlgorithmCase(unittest.TestCase):

    def test_first_table(self):
        num_table = np.array([
            [5, 20, 8, -15],
            [3, 4, 7, -6],
            [-9, -12, 10, 7],
            [1, -5, 3, 9]
        ])
        expected_table = np.array([
            [5, 20, 8, 0],
            [3, 4, 7, -6],
            [0, -12, 10, 7],
            [1, 0, 3, 9]
        ])
        cards = 4
        start_index = 3
        hidden_items = A_algorithm.algorithm(num_table, cards, start_index)
        hidden_coords = A_algorithm.get_hidden_coords(hidden_items)
        result_table = table.get_result(num_table, hidden_coords)
        self.assertEqual(is_acceptable(hidden_items), True)
        self.assertEqual(table.get_sum_of_elements(expected_table), table.get_sum_of_elements(result_table))
        self.assertEqual(np.array_equal(expected_table, result_table), True)

    def test_second_table(self):
        num_table = np.array([
            [5, 1, -4, -9],
            [3, 4, 1, -6],
            [-9, -12, 10, 7],
            [1, -5, 3, 9]
        ])
        expected_table = np.array([
            [5, 1, 0, -9],
            [3, 4, 1, 0],
            [0, -12, 10, 7],
            [1, 0, 3, 9]
        ])
        cards = 4
        start_index = 1
        hidden_items = A_algorithm.algorithm(num_table, cards, start_index)
        hidden_coords = A_algorithm.get_hidden_coords(hidden_items)
        result_table = table.get_result(num_table, hidden_coords)
        self.assertEqual(is_acceptable(hidden_items), True)
        self.assertEqual(table.get_sum_of_elements(expected_table), table.get_sum_of_elements(result_table))
        self.assertEqual(np.array_equal(expected_table, result_table), True)

    def test_third_table(self):
        num_table = np.array([
            [5, 1, -4, -15],
            [3, 4, 1, -6],
            [-9, -15, 10, 7],
            [1, -5, 3, 9]
        ])
        expected_table = np.array([
            [5, 1, -4, 0],
            [3, 4, 1, -6],
            [-9, 0, 10, 7],
            [1, -5, 3, 9]
        ])
        cards = 10
        start_index = 3
        hidden_items = A_algorithm.algorithm(num_table, cards, start_index)
        hidden_coords = A_algorithm.get_hidden_coords(hidden_items)
        result_table = table.get_result(num_table, hidden_coords)
        self.assertEqual(is_acceptable(hidden_items), True)
        self.assertEqual(table.get_sum_of_elements(expected_table), table.get_sum_of_elements(result_table))
        self.assertEqual(np.array_equal(expected_table, result_table), True)


class NaiveAlgorithmCase(unittest.TestCase):

    def test_first_table(self):
        num_table = np.array([
            [5, 20, -8, -10],
            [3, 4, 7, -6],
            [-9, -10, 10, 7],
            [1, -2, 3, 9]
        ])
        expected_table = np.array([
            [5, 20, -8, 0],
            [3, 4, 7, -6],
            [-9, 0, 10, 7],
            [1, -2, 3, 9]
        ])
        cards = 4
        hidden_items = naive_alogrithm.naive_algorithm(num_table, cards)
        result_table = table.get_result(num_table, hidden_items)
        self.assertEqual(table.get_sum_of_elements(expected_table), table.get_sum_of_elements(result_table))
        self.assertEqual(np.array_equal(expected_table, result_table), True)

if __name__ == '__main__':
    unittest.main()

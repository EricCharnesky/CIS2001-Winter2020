from unittest import TestCase
import MidtermReview

class TestSum_of_even_columns(TestCase):
    def test_sum_of_even_columns(self):
        expected_sum = 24
        two_dimensional_list = [
            [1,2,3,4],
            [5,6,7,8],
            [1,2,1,2]
        ]

        actual_sum = MidtermReview.sum_of_even_columns(two_dimensional_list)

        self.assertEqual(expected_sum, actual_sum)

    def test_sum_of_even_columns2(self):
        expected_sum = 30
        two_dimensional_list = [
            [1,2,3,4],
            [5,6,2,8],
            [1,2,1,2]
        ]

        actual_sum = MidtermReview.sum_of_even_columns(two_dimensional_list)

        self.assertEqual(expected_sum, actual_sum)


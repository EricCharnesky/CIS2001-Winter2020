from unittest import TestCase
from January16th import Assignment, AdjustedAssignment

class TestAssignment(TestCase):

    def test_get_average_score(self):
        # AAA

        # arrange
        score1 = 10
        score2 = 20
        score3 = 30
        expected_average_score = 20
        assignment = Assignment()
        assignment.add_score(score1)
        assignment.add_score(score2)
        assignment.add_score(score3)

        # act
        actual_average_score = assignment.get_average_score()

        # assert
        self.assertEqual(expected_average_score, actual_average_score)

    def test_get_min_score(self):
        # AAA

        # arrange
        score1 = 10
        score2 = 20
        score3 = 30
        expected_min_score = 10
        assignment = Assignment()
        assignment.add_score(score1)
        assignment.add_score(score2)
        assignment.add_score(score3)

        # act
        actual_min_score = assignment.get_min_score()

        # assert
        self.assertEqual(expected_min_score, actual_min_score)

    def test_get_max_score(self):
        # AAA

        # arrange
        score1 = 10
        score2 = 20
        score3 = 30
        expected_max_score = 30
        assignment = Assignment()
        assignment.add_score(score1)
        assignment.add_score(score2)
        assignment.add_score(score3)

        # act
        actual_max_score = assignment.get_max_score()

        # assert
        self.assertEqual(expected_max_score, actual_max_score)

    def test_get_adjusted_average_score(self):
        # AAA

        # arrange
        score1 = 10
        score2 = 20
        score3 = 30
        expected_average_score = 90
        assignment = AdjustedAssignment()
        assignment.add_score(score1)
        assignment.add_score(score2)
        assignment.add_score(score3)

        # act
        actual_average_score = assignment.get_average_score()

        # assert
        self.assertEqual(expected_average_score, actual_average_score)

    def test_get_adjusted_min_score(self):
        # AAA

        # arrange
        score1 = 10
        score2 = 20
        score3 = 30
        expected_min_score = 80
        assignment = AdjustedAssignment()
        assignment.add_score(score1)
        assignment.add_score(score2)
        assignment.add_score(score3)

        # act
        actual_min_score = assignment.get_min_score()

        # assert
        self.assertEqual(expected_min_score, actual_min_score)

    def test_get_adjusted_max_score(self):
        # AAA

        # arrange
        score1 = 10
        score2 = 20
        score3 = 30
        expected_max_score = 100
        assignment = AdjustedAssignment()
        assignment.add_score(score1)
        assignment.add_score(score2)
        assignment.add_score(score3)

        # act
        actual_max_score = assignment.get_max_score()

        # assert
        self.assertEqual(expected_max_score, actual_max_score)

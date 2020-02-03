import copy


class GradeBook:

    def __init__(self):
        self.final_exam = None
        self.midterm_exam = None
        self.project = None

    def get_average_score(self):
        return ( self.final_exam.get_adjusted_average_score() +
            self.midterm_exam.get_adjusted_average_score() +
            self.project.get_adjusted_average_score() ) / 3

class Assignment:

    def __init__(self):
        self._scores = []

    def add_score(self, score):
        if type(score) != int:
            raise ValueError("score must be int")
        self._scores.append(score)

    def get_average_score(self):
        return sum(self._scores) / len(self._scores)

    def get_max_score(self):
        return max(self._scores)

    def get_min_score(self):
        return min(self._scores)

    def print_assignment(self):
        print("assignment")


class AdjustedAssignment(Assignment):

    def get_max_score(self):
        return 100

    def get_average_score(self):
        difference_between_100_and_max = self._get_adjustment()
        return super().get_average_score() + difference_between_100_and_max

    def _get_adjustment(self):
        max_score = max(self._scores)
        difference_between_100_and_max = 100 - max_score
        return difference_between_100_and_max

    def get_min_score(self):
        difference_between_100_and_max = self._get_adjustment()
        return super().get_min_score() + difference_between_100_and_max

    # overrides the base Object class __str__ method
    def __str__(self):
        return "I'm an assignment!"

first_assignment = AdjustedAssignment()
first_assignment.add_score(90)
first_assignment.add_score(101)
first_assignment.add_score(79)

print(first_assignment)

second_assignment = copy.deepcopy(first_assignment)

second_assignment.add_score(23)

third_assignment = AdjustedAssignment()
third_assignment.add_score(100)

gradebook = GradeBook()
gradebook.midterm_exam = copy.deepcopy(first_assignment)
gradebook.final_exam = copy.deepcopy(second_assignment)
gradebook.project = copy.deepcopy(third_assignment)

another_gradebook = copy.deepcopy(gradebook)

first_assignment.add_score(60)

output = first_assignment.print_assignment()


print("please wait")
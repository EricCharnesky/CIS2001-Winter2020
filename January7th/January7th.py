class Grade:

    def __init__(self, score):
        self._score = score

    def get_score(self):
        return self._score

    def get_letter_grade(self):
        return self._get_letter_grade(self._score)

    def _get_letter_grade(self, score):
        if score > 93:
            return 'A'
        if score >= 90:
            return 'A-'
        if score >= 87:
            return "B+"
        if score >= 83:
            return 'B'
        if score >= 80:
            return 'B-'
        if score >= 77:
            return "c+"
        if score >= 73:
            return 'C'
        if score >= 70:
            return 'C-'
        if score >= 67:
            return "D+"
        if score >= 63:
            return 'D'
        if score >= 60:
            return 'D-'
        return 'E'


class AdjustedGrade(Grade):

    def __init__(self, score):
        Grade.__init__(self, score)
        self._adjustment = 0

    def set_grade_adjustment(self, adjustment):
        if adjustment > 100:
            raise ValueError("The adjustment can't be more than 100")
        self._adjustment = adjustment

    def get_grade_adjustment(self):
        return self._adjustment

    def get_letter_grade(self):
        return self._get_letter_grade(self.score + self._adjustment)


score = int(input("Enter a score"))
my_score = Grade(score)
print(my_score.get_letter_grade())

my_adjusted_score = AdjustedGrade(score)
my_adjusted_score.get_letter_grade()




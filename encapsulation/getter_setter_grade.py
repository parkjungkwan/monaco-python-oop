class Grade(object):

    def __init__(self):
        self._name = ''
        self._korean = 0
        self._english = 0
        self._math = 0

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def korean(self) -> str:
        return self._korean

    @korean.setter
    def korean(self, korean):
        self._korean = korean

    @property
    def english(self) -> str:
        return self._english

    @english.setter
    def english(self, english):
        self._english = english

    @property
    def math(self) -> str:
        return self._math

    @math.setter
    def math(self, math):
        self._math = math


class Exam(Grade):

    def __init__(self):
        self.korean = Grade()
        self.english = Grade()
        self.math = Grade()

    def sum(self):
        return self.korean + self.english + self.math

    def avg(self):
        return self.sum() / 3

    @staticmethod
    def main():
        exam = Exam()
        exam.korean = 40
        exam.english = 49
        exam.math = 59

        print(f'합계 : { exam.sum() } 점, 평균 : { int(exam.avg()) }')


if __name__ == '__main__':
    Exam.main()
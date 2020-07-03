class Question(object):
        def __init__(self, title, question_list, answer):
            self.title = title # string
            self.question_list = question_list # list of strings
            self.answer = answer # string (or index into list?)

        def check(self, proposed_answer):
            if proposed_answer == self.answer: 
                return True
            return False

        def __str__(self):
            s = self.title + ":\n"
            letters = "ABCDEFG"
            for i, q in enumerate(self.question_list):
                s += letters[i] + ": " + q + "\n"
            s += "Correct answer is: " + self.answer
            return s


class Question_set(object):
    def __init__(self, name):
        self.name = name
        self.qset = []

    def read(self, file_name):
        pass

    def write(self, file_name):
        pass
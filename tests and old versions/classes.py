class Question(object): #models a single question
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


class Question_set(object): #list of question objects (similar Polygons having a list of Points in HCI 574).
                            # read/write from/to a file.
    def __init__(self, name):
        self.name = name
        self.qset = []

    def read(self, name):
        import csv
        #questions = [] # creates question list
        with open('questions.csv', 'r') as csvfile: # opens the .txt file in same folder
            readCSV = csv.reader(csvfile)# read lines in .txt file
            questionString = []
            answers = [] # answers list
            correctLetter = []
            header = next(readCSV)
            for row in readCSV:
                questionString = [row[0]]
                answers = [row[1:-1]]
                correctLetter = [row[-1]]

            questionString.append(questionString)
            answers.append(answers)
            correctLetter.append(correctLetter)

        # questions.append(questionString + answers + correctLetter)
            #print(questions)
            #questions.append(answers)
            #questions.append(correctLetter)

        csvfile.close() # close file

    #def write(self, file_name):
        #pass
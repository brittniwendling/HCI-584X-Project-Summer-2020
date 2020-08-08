
# reads from questions file
import csv
questions = [] # creates question list
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

    questions.append(questionString)
    questions.append(answers)
    questions.append(correctLetter)

    print(questions)
csvfile.close() # close file

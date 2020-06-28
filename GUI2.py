#This will be for the GUI that will create, save, and load the questions and answers files
# This version will save and load the data a user inputs into a file, which the quiz app will run

#pickle module
import pickle
import os
os.system("clear")

#create a list of questions (users will input on GUI)
questions = ["Question 1, Question 2, Question 3"]

#create a list of answers (users will input on GUI)
answers = ["Answer 1, Answer 2, Answer 3"]

#save the questions 
pickle.dump(questions, open("questions.dat", "wb")) #write data

#save the answers
pickle.dump(answers, open("answers.dat", "wb")) #write data

#load the saved questions
questions = pickle.load(open("questions.dat", "rb")) #read data

#load the saved answers 
answers = pickle.load(open("answers.dat", "rb")) #read data

print(questions)
print(answers)
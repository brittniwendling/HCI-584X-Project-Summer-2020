#-------------------------------------------------------------------------------
# Name:      main.py
# Purpose:   Primary program flow for Quiz Application
# Author(s): Brittni Wendling
# Created:   06/09/2020
#-------------------------------------------------------------------------------

#imports tkinter
import tkinter as tk 

# eventually use for keeping track of running time 
# from time import datetime

# create Question class
class Question:
    def __init__(self, question, answers, correctLetter): # question, answers, correct answer letter
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

# check answers for correctness function
    def check(self, letter, view):
        num_right = 0
        points = 0
        if(letter == self.correctLetter):
            label = tk.Label(view, text="Correct! +10 points!")
            num_right = num_right + 1 # 1 right num added
            points = points + 10 # add 10 points
        else:
            label = tk.Label(view, text="Incorrect! -5 points")
            points = points - 5 # loses 5 points
        label.pack()
        view.after(1000, lambda *args: self.unpackView(view))


    def getView(self, window):
        view = tk.Frame(window)

        # button widget creation
        label = tk.Label(view, text=self.question)
        button_a = tk.Button(view, text=self.answers[0], command=lambda *args: self.check("A", view))
        button_b = tk.Button(view, text=self.answers[1], command=lambda *args: self.check("B", view))
        button_c = tk.Button(view, text=self.answers[2], command=lambda *args: self.check("C", view))
        button_d = tk.Button(view, text=self.answers[3], command=lambda *args: self.check("D", view))

        # button widget layout
        label.pack()
        button_a.pack()
        button_b.pack()
        button_c.pack()
        button_d.pack()
        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()

# ask question function
def askQuestion():
    global questions, window, index, button, num_right, number_of_questions, points 
    if(len(questions) == index + 1): #if last question has been answered
        tk.Label(window, text="Congratulations - you finished the quiz! " + str(num_right) + " of " + str(number_of_questions) + " questions were answered correctly. Nice work!").pack() # show questions correct
        tk.Label(window, text="Total number of points:" + str(points)).pack() # show total points
        return
    begin_button.pack_forget()
    index = index + 1
    questions[index].getView(window).pack()

questions = [] # question list
file = open("questions.txt", "r") # opens the .txt file in same folder
line = file.readline() # read lines in .txt file
while(line != ""): # line not empty
    questionString = line
    answers = [] # answers list
    for i in range (4): # creates answers grouping
        answers.append(file.readline()) # add answers grouping to answers list

    correctLetter = file.readline()
    correctLetter = correctLetter[:-1] # last line of answers grouping is correct answer
    questions.append(Question(questionString, answers, correctLetter))
    line = file.readline()
file.close() # close file
index = -1 # index counter
num_right = 0 # number right counter 
points = 0 # total points counter
number_of_questions = len(questions) #total questions in set

window = tk.Tk() # tkinter window
begin_button = tk.Button(window, text="Begin Quiz", command=askQuestion) # Begin Quiz button
begin_button.pack()
quit_button = tk.Button(window,text="Quit Quiz", command=window.quit) # Quit Quiz button
quit_button.pack()
window.mainloop()

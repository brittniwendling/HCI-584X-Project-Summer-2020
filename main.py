#-------------------------------------------------------------------------------
# Name:      main.py
# Purpose:   Primary program flow for Quiz Application
# Author(s): Brittni Wendling
# Created:   06/09/2020
#-------------------------------------------------------------------------------

#imports tkinter
from tkinter import *
import tkinter as tk 

#imports time
import time 

# create Question class
class Question:
    def __init__(self, question, answers, correctLetter): # question, answers, correct answer letter
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

# check answers for correctness function
    def check(self, letter, view):
        global num_right
        global points
        if(letter == self.correctLetter):
            label = tk.Label(view, text="Correct! +10 points!", font='Helvetica 14 bold')
            num_right = num_right + 1 # 1 right num added
            points = points + 10 # add 10 points
        else:
            label = tk.Label(view, text="Incorrect! -5 points", font='Helvetica 14 bold')
            points = points - 5 # loses 5 points
        label.pack()
        view.after(1000, lambda *args: self.unpackView(view))


    def getView(self, root):
        view = tk.Frame(root)

        # answer button widget creation
        label = tk.Label(view, text=self.question)
        button_a = tk.Button(view, text=self.answers[0], command=lambda *args: self.check("A", view))
        button_b = tk.Button(view, text=self.answers[1], command=lambda *args: self.check("B", view))
        button_c = tk.Button(view, text=self.answers[2], command=lambda *args: self.check("C", view))
        button_d = tk.Button(view, text=self.answers[3], command=lambda *args: self.check("D", view))

        # answer button widget layout
        label.pack()
        button_a.pack()
        button_b.pack()
        button_c.pack()
        button_d.pack()
        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()
   

# ask a question function
start_time = time.time() #starts time with current time
def askQuestion():
    global questions, root, index, button, num_right, number_of_questions, points 
    if(len(questions) == index + 1): #if last question has been answered
        tk.Label(root, text="Congratulations - you finished the quiz! " + str(num_right) + " of " + str(number_of_questions) + " questions were answered correctly. Nice work!").pack() # show questions correct
        tk.Label(root, text="Total number of points:" + str(points) + "out of" + str(points_possible)).pack() # show total points
        elapsed_time = time.time() - start_time
        time.strftime("%H:%M:%S", time.gmtime(elapsed_time)) # formats elapsed time 
        tk.Label(root, text="Total elapsed time:"+ str(elapsed_time)).pack() # makes label for elapsed time
        return
    begin_button.pack_forget()
    index = index + 1
    questions[index].getView(root).pack()

# reads from questions file
questions = [] # creates question list
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

# Counters
index = -1 # index counter
num_right = 0 # number right counter
points = 0 # number points counter 
number_of_questions = len(questions) #total questions in set
points_possible = number_of_questions * 10 #total points possible

##### main:
root = tk.Tk() # creates main tkinter window
root.geometry('500x500') #sets size of tk window
root.title("StudyStar⭐️") #root title
#root.configure(background = "black") #changes background color

#Welcome message
tk.Label(root, text="Welcome to StudyStar⭐️ - Let's get studying!", font='Helvetica 18 bold').pack()

# Set Question Set Name
def set_qset_name():
    qset_name = textentry.get()
    tk.Label(root, text="Your Question Set Name Is:" + qset_name).pack() 
qset_label = tk.Label(root, text="Enter a name for your question set:").pack() 
textentry = Entry(root, width = 20, bg="black", fg="white")
textentry.pack()
qset_name_button = tk.Button(root, text="Submit", width=6, command=set_qset_name).pack()

# Begin Quiz button
begin_button = tk.Button(root, text="Begin Quiz", command=askQuestion, ) 
begin_button.pack()

# Quit Quiz button
quit_button = tk.Button(root,text="Quit Quiz", command=root.quit) 
quit_button.pack()

# Replay button
replay_button = tk.Button(root,text="Play Again", command=None)
replay_button.pack()


root.mainloop() #loops the main tkinter window





#-------------------------------------------------------------------------------
# Name:      main.py
# Purpose:   Primary program flow for StudyStar⭐️ Quiz Application
# Author(s): Brittni Wendling
# Created:   06/09/2020
#-------------------------------------------------------------------------------
import sys
import os

#imports tkinter
from tkinter import * 
from tkinter import messagebox
import tkinter as tk 

#imports time
import time 
import datetime

##### main:
root = tk.Tk() # creates main tkinter window
root.geometry('550x250') #sets size of tk window
root.title("StudyStar⭐️") #window title
#root.configure(background = "black") #changes background color

# Welcome message
tk.Label(root, text="Welcome to StudyStar⭐️", font='Helvetica 14 bold').grid(row=1, column=0, columnspan=2)

# show instructions for StudyStar⭐️
def about():
    messagebox.showinfo(title="About StudyStar⭐️",message="Put instructions for StudyStar⭐️ here! ").grid
    return

# Clock
def clock():
    hour = time.strftime("%H") #hour
    minute = time.strftime("%M") #minute
    second = time.strftime("%S") #second
    am_pm = time.strftime("%p") #am or pm

    clock_label.config(text=hour + ":" + minute + ":" + second + " " + am_pm)
    clock_label.after(1000, clock)

clock_label = tk.Label(root, text="",font='Helvetica,bold', fg="white", bg="black")
clock_label.grid(row = 0, column=0, columnspan=2)

# Run Clock function    
clock()

# Set Question Set Name
def set_qset_name():
    qset_name = textentry.get()
    tk.Label(root, text="Your Question Set Name Is:" + " " + qset_name, font='Helvetica').grid(row=3, column=0)
    #tk.Label(root,text = "Your Questions are coming from the file: questions.txt", font='Helvetica' ).grid(row=2, column=0) #eventually this will be updated w/ 2nd GUI?
    begin_button.grid(row=4, column=0)
    qset_name_button.grid_forget()# Submit qset name button disappears
    qset_label.grid_forget() # qset label disappears
    textentry.grid_forget() # qset name entry disappears 
qset_label = tk.Label(root, text="Enter a name for your question set:", font='Helvetica')
qset_label.grid(row=2, column=0)
textentry = Entry(root,font='Helvetica', bg="black", fg="white")
textentry.grid(row=2, column=1)
qset_name_button = tk.Button(root, text="Submit", font='Helvetica', command=set_qset_name)#Submit button
qset_name_button.grid(row=2, column=2)
about_button = tk.Button(root, text="Instructions", font='Helvetica', command=about) #Instructions button
about_button.grid(row=1, column=4)

# create Question class
class Question:
    def __init__(self, question, answers, correctLetter): # question, answers, correct answer letter
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

    # check answers for correctness function
    def check(self, letter, view):
        global num_right   # CH Don't use globals for that! check() should just return True/False (or 1/0)
        global points      # and what ever called check() should update num_right then
                           # If you want to do the update here, give check num_right as an arg and return it
        global tries
        while True:
            if(letter == self.correctLetter): # correct answer
                tk.Label(view, text="CORRECT! +10 points!", font='Helvetica,bold', fg="green").grid(row=11, column=0, columnspan=2)
                num_right = num_right + 1 # 1 right num added  # CH do this "outside"
                points = points + 10 # add 10 points
                stop_asking = False
                tries = 2 #tries is reset to 2 for next question
                break
           
            tries = tries - 1 #lose a try if answer is wrong
    
            if tries == 0: # 0 tries left      
                tk.Label(view, text='INCORRECT! You ran out of your attempts.', font='Helvetica,bold', fg="red").grid(row=13, column=0, columnspan=2)
                points = points - 5 #lose 5 points
                stop_asking = True
                tries = 2 #tries is reset to 2 for next question
                break
                
            tk.Label(view, text='INCORRECT! -5 points! Try again. You have' + " " + str(tries) + " " + "attempt remaining.", font='Helvetica,bold', fg="red").grid(row=12, column=0, columnspan=2)
            points = points - 5 #lose 5 points
            if stop_asking:
                tries = 2 #tries is reset to 2 for next question
                break
                
        view.after(1000, lambda *args: self.unpackView(view)) # time delay between questions

    def getView(self, root):
        view = tk.Frame(root)
    
        # answer button widget creation
        label = tk.Label(view, text=self.question)
        button_a = tk.Button(view, text=self.answers[0], command=lambda *args: self.check("A", view))
        button_b = tk.Button(view, text=self.answers[1], command=lambda *args: self.check("B", view))
        button_c = tk.Button(view, text=self.answers[2], command=lambda *args: self.check("C", view))
        button_d = tk.Button(view, text=self.answers[3], command=lambda *args: self.check("D", view))

        # answer button widget layout
        label.grid(row=5, column=0, columnspan=2)
        button_a.grid(row=6, column=0)
        button_b.grid(row=6, column=1)
        button_c.grid(row=7, column=0)
        button_d.grid(row=7, column=1)
        return view

    def unpackView(self, view):
        view.grid_forget()
        askQuestion()

#start_time = time.time() #starts time with current time

# ask a question function
def askQuestion():  
    global questions, root, index, button, num_right, number_of_questions, points 
    if(len(questions) == index + 1): #if last question has been answered
        tk.Label(root, text="Congratulations - you finished the quiz! ").grid(row=3) # show questions correct
        tk.Label(root, text=str(num_right) + " out of " + str(number_of_questions) + " questions were answered correctly.").grid(row=4)
        tk.Label(root, text="Total number of points:" + " " + str(points) + " " + "out of" + " " + str(points_possible)).grid(row=5) # show total points
        #elapsed_time = time.time() - start_time
        #time.strftime("%H:%M:%S", time.gmtime(elapsed_time)) # formats elapsed time 
        #tk.Label(root, text="Total elapsed time:"+ " " + str(elapsed_time)).pack() # makes label for elapsed time
        # Replay button
        replay_button = tk.Button(root,text="Study Again", command=None)
        replay_button.grid(row=3, column=4)
        return

    begin_button.grid_forget() #Begin quiz button disappears
    qset_name_button.grid_forget()#Submit qset name button disappears
    qset_label.grid_forget() #qset label disappears
    textentry.grid_forget() # qset name entry disappears
    
    index = index + 1
    questions[index].getView(root).grid(row=2)
    
# reads from questions file
questions = [] # creates question list
file = open("questions.txt", "r") # opens the .txt file in same folder
                                    #eventually the file will come from the 2nd GUI!
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
tries = 2 #number tries counter

number_of_questions = len(questions) #total questions in set
points_possible = number_of_questions * 10 #total points possible

# CH this button could eventually become an app class that you instantiate here and give window as an arg ...
# Begin Quiz button
begin_button = tk.Button(root, text="Begin Studying",font='Helvetica', command=askQuestion) 

# Quit Quiz button
quit_button = tk.Button(root,text="Quit Quiz", font='Helvetica', fg="red", command=root.quit) 
quit_button.grid(row=0, column=4)

root.mainloop() #loops the main tkinter window





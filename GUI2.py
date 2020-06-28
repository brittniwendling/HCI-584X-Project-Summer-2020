
import sys
import os

#This will be for the GUI that will create and save the questions and answers into {qset_name}questions.dat files
#This version will save and load the data a user inputs into a file, which the other GUI quiz app will run

#pickle module
import pickle
import os

#imports tkinter
from tkinter import *
from tkinter import messagebox
import tkinter as tk 

#imports time
import time 

##### main:
root = tk.Tk() # creates main tkinter window
root.geometry('800x400') #sets size of tk window
root.title("StudyStar⭐️ Quiz/Answers Creator") #window title
#root.configure(background = "black") #changes background color

#Welcome message
tk.Label(root, text="Welcome to StudyStar⭐️ Questions/Answers creator!", font='Helvetica 30 bold').pack()

# show instructions for StudyStar⭐️
def about():
    messagebox.showinfo(title="About StudyStar⭐️",message="Put instructions for StudyStar⭐️ here! ")
    return

# Set Question Set Name
qset_label = tk.Label(root, text="Enter a name for your question set:", font='Helvetica 18')
qset_label.pack() 
def set_qset_name():
    qset_name = textentry.get()
    tk.Label(root, text="Your Question Set Name Is:" + qset_name, font='Helvetica 18').pack()
    qset_name_button.pack_forget()#Submit qset name button disappears
    qset_label.pack_forget() #qset label disappears
    textentry.pack_forget() # qset name entry disappears 

textentry = Entry(root, width = 20, bg="black", fg="white")
textentry.pack()
qset_name_button = tk.Button(root, text="Submit", width=6, command=set_qset_name)#Submit button
qset_name_button.pack()
about_button = tk.Button(root, text="Instructions", command=about) #Instructions button
about_button.pack(side = BOTTOM)

#create a list of questions (users will input on GUI)
questions = []

#create a list of answers (users will input on GUI)
answers = []

q1_label = tk.Label(root, text="Enter Question 1:", font='Helvetica 18')
q1_label.pack()
question1_entry = Entry(root, width = 20, bg="black", fg="white")
question1_entry.pack()
question1 = [question1_entry.get()] 
question1.append(questions) #add question 1 to questions list
a1_label = tk.Label(root, text="Enter Answer 1:", font='Helvetica 18')
a1_label.pack()
answer1_entry =Entry(root, width = 20, bg="black", fg="white")
answer1_entry.pack()
answer1 = [answer1_entry.get()]
answer1.append(answers) #add answer 1 to answers list

#save the questions 
pickle.dump(questions, open("questions.dat", "wb")) #write data

#save the answers
pickle.dump(answers, open("answers.dat", "wb")) #write data

#load the saved questions
questions = pickle.load(open("questions.dat", "rb")) #read data

#load the saved answers 
answers = pickle.load(open("answers.dat", "rb")) #read data

#Next button
next_button = tk.Button(root, text="Enter Next", command=None) 
next_button.pack()

#Save/Exit button
save_button = tk.Button(root, text="Save and Exit", command=None) 
save_button.pack()

# Quit button
quit_button = tk.Button(root,text="Quit", command=root.quit) 
quit_button.pack(side = BOTTOM)

print(questions)
print(answers)


root.mainloop()
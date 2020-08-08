#manage the user flow and use the question_set class. All GUI stuff here!!!!

from tkinter import * # import everything from module and put into global namespace
from tkinter import messagebox

from classes import Question, Question_set

# test
q = Question("What color is a lemon?", ["blue", "limonetta", "yellow"], "C")
print(q.check("blue"))
print(q)

class Quiz_app(object):
    def __init__(self, master): #
        self.master = master # attribute to store link to the window that App is inside of (need it later)
        self.frame = Frame(self.master)
        self.frame.grid(row=0, column=0)
        self.load_qset_GUI()
        self.index = -1
        self.num_right = 0
        self.points = 0
        self.tries = 2
        #self.number_of_questions = len(questionString)
        #self.points_possible = self.number_of_questions * 10 #total points possible
        self.master.geometry('550x250') #sets size of tk window
        self.master.title("StudyStar⭐️") #window title
        #root.configure(background = "black") #changes background color


  # show instructions for StudyStar⭐️
    def about(self):
        messagebox.showinfo(title="About StudyStar⭐️",message="Put instructions for StudyStar⭐️ here! ")
        return

    def load_qset_GUI(self):
        # I don't need to make the Label and Button attributes here b/c I don't need to talk to them later and
        # they are inside the Frame when they are destroyed later. But, if you need to config them later you must
        # make the attributes!
        welcome_label = Label(self.frame, text="Welcome to StudyStar⭐️", font='Helvetica 14 bold').grid(row=1, column=0)
        qset_label = Label(self.frame, text="Name for question set:")
        qset_label.grid(row=2, column=0, columnspan=1)
        self.qset_name_entry = Entry(self.frame, width=20) # I DO need the entry widget as attribute so I can get it's text later!
        self.qset_name_entry.grid(row=2, column=1, columnspan=1)
        qset_name_button = Button(self.frame, text="Load", width=6, command=self.read_qset) 
        qset_name_button.grid(row=2, column=2, columnspan=1)
        #Instructions button
        self.about_button = Button(self.frame, text = "Instructions", command = self.about)
        self.about_button.grid(row=1, column=4)
        # Begin Quiz button
        self.begin_button = Button(self.frame, text="Begin Studying",font='Helvetica', command=None) #self.askQuestion
        # Quit Quiz button
        self.quit_button = Button(self.frame,text="Quit Quiz", font='Helvetica', fg="red", command=self.frame.quit) 
        self.quit_button.grid(row=0, column=4)


    def read_qset(self):
        file_name = self.qset_name_entry.get()
        print("reading in", file_name)
        #Label(self.frame, text= "Reading in: {fname}"
        self.qset = Question_set(file_name)
###NEED TO ADD A COMMAND TO THE LOAD BUTTON 


    




# run app
master = Tk()  # create a Tk window object, call it master
app = Quiz_app(master) # create an App object inside the master window
master.mainloop() # have the master window go live, loop until quit
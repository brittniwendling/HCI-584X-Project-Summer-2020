from tkinter import * # import everything from module and put into global namespace

from classes import Question, Question_set

# test
q = Question("What color is a lemon?", ["Blue", "limonetta", "yellow"], "C")
print(q.check("Blue"))
print(q)


class Quiz_app(object):
    def __init__(self, master): #
        self.master = master # attribute to store link to the window that App is inside of (need it later)
        self.frame = Frame(self.master)
        self.frame.pack(side="top", fill="both", expand=True)
        self.load_qset_GUI()

    def load_qset_GUI(self):
        # I don't need to make the Labels attributes here b/c I don't need to talk to them later and
        # they are inside the Frame when they are destroyed later. But, if you need to config them later you must
        # make the attributes!
        qset_label = Label(self.frame, text="Name for question set:")
        qset_label.grid(row=0, column=0, columnspan=1)
        self.qset_name_entry = Entry(self.frame, width=20) # I DO need the entry widget as attribute so I can get it's text later!
        self.qset_name_entry.grid(row=0, column=1, columnspan=1)
        qset_name_button = Button(self.frame, text="Load", width=6, command=self.read_qset) 
        qset_name_button.grid(row=0, column=2, columnspan=1)

    def read_qset(self):
        fname = self.qset_name_entry.get()
        print("reading in", fname)
        self.qset = Question_set(fname)

        # destroy frame
        self.frame.destroy()

        # pretend we want to start over again
        self.frame = Frame(self.master)
        self.frame.pack(side="top", fill="both", expand=True)
        self.load_qset_GUI()





# run app
master = Tk()  # create a Tk window object, call it master
app = Quiz_app(master) # create an App object inside the master window
master.mainloop() # have the master window go live, loop until quit
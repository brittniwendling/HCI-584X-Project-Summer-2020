#-------------------------------------------------------------------------------
# Name:      CreateQuizApp.py
# Purpose:   Primary program flow for creating the StudyStar⭐️ Quiz Application
# Author(s): Brittni Wendling
# Created:   06/09/2020
# Updated:   08/07/2020
#-------------------------------------------------------------------------------

"""
This module handles the primary program flow for StudyStar⭐️ and the GUI interface.
It is used in the main.py file.
"""

# import the required internal modules
import QuestionsModel as qm

# import the required external modules
from tkinter import * 
import tkinter as tk
from tkinter import messagebox # necessary for the Instructions dialogue box
from tkinter import ttk # necessary for the Progressbar widget
from tkinter import filedialog # necessary for user's self-selecting .csv files
import time # necessary for clock function

class MainQuizApp():
	""" Main application class.

    Most of the navigation classes and functions, as well as StudyStar⭐️ GUI display code are located in this class.
	"""
	def __init__(self, questions_file=''):
		self.filename = questions_file # .csv file
		self._build_gui() # build_gui function
		self.clock() # clock function
		self.current_question_index=0 # question index counter
		self.points = 0 # number points counter
		self.num_right = 0 # number questions correct counter
		self.tries = 2 # number tries counter
		self.user_answer = tk.IntVar() # user's answer
		self.root.mainloop() # have the root window go live, loop until quit

	def about(self):
		"""
		Function to displays the instructions for StudyStar⭐️ in a messagebox.

		Returns:
			tkinter messagebox with instructions for the quiz
		"""
		messagebox.showinfo(title="About StudyStar⭐️", message=('Welcome to StudyStar⭐️ - an app for all your studying needs! '
		 							'To begin studying, please click the “Load File and Start Quiz” button. '
		 							'This button will open up a file selector where you can choose any .csv file to run through the app. '
		 							'Please see the ReadMe.md for full information on how the question set file will need to '
									'be structured in order to work properly with the app. After you choose your .csv file to load, StudyStar⭐️ '  
									'will automatically begin the quiz. One question will be shown at a time, where you will '
									'choose your answer and click the “Check Answer” button. You will then be provided with '
									'feedback on whether your answer was correct. A progress bar is shown at the bottom of the quiz, '
									'which shows you real-time feedback of your progress towards finishing the quiz. '
									'Once you answer all of the questions, you will be shown how many questions you got right '
									'and your total score! Exit the quiz at any time by clicking the “Quit Quiz” button in the top right corner. '
									'Have fun, and good luck studying!'))
		return
	
	def browse_files(self):
		"""
		Function that allows the user to select a .csv file using a filedialog box.
		Stores this .csv into variable called self.filename to be used throughout quiz.
		"""
		self.filename = filedialog.askopenfilename(initialdir="", title="Select a csv file:", filetypes=[("csv files", "*.csv"), ("all files", "*.*")])

	def get_question(self):
		"""
		Function that pulls the question string objects from the selected .csv file.

		Returns:
			questions from the .csv questions set, 1 at a time
		"""
		return self.questions[self.current_question_index][0]

	def get_options(self):
		"""
		Function that pulls the question choice string objects from the selected .csv file.

		Returns:
			answer choice options for each question from the .csv questions set
		"""
		print(self.current_question_index)
		print(self.questions[self.current_question_index])
		return self.questions[self.current_question_index][1:-1]

	def get_current_answer(self):
		"""
		Function that pulls the correct answer strings from the selected .csv file.

		Returns:
			correct answer option for each question from the .csv questions set
		"""
		return self.questions[self.current_question_index][-1]

	def start(self):
		"""
		Function that begins the quiz and starts showing questions along with their option choices.
		"""
		# get questions
		self.questions = qm.get_questions(self.filename) # get_question function on the .csv file user selected
		current_question = self.get_question()
		self._update_question(current_question)
		
		# get options
		options = self.get_options()
		self._make_options(options)
		
		self.qset_name_button.grid_forget() # hide load and start button
		self.qset_name_label.grid_forget() # hide qset name label
		
		# show sumbit button and format questions box
		self.submit_button.grid(row=6) # show check answer button
		self.questions_box.grid(row=2,column=0) # show questions box
		
		# create progress bar
		self.my_progress = ttk.Progressbar(self.root, orient=HORIZONTAL,length=400, mode='determinate')
		self.my_progress.grid(row=12, column=0, columnspan=3, padx=20, pady=10)

		# variables for progress bar and end of quiz
		self.number_of_questions = len(self.questions) # total number questions in set
		self.points_possible = self.number_of_questions * 10 #total points possible

	def step(self):
		"""
		Function that increases the step of progress bar in relation to how many questions are in the question set.
		"""
		self.my_progress['value'] += 100/self.number_of_questions
		#print(self.my_progress['value']) #DEBUG

	def is_answer_correct(self):
		"""
		Function that checks whether a selected answer is correct.

		Returns:
			True if answer selected matches correct answer
		"""
		return self.get_current_answer() == self.get_options()[self.user_answer.get()-1]

	def _update_answer_label(self):
		"""
		Function that updates the answer label shown as correct/incorrect and updates the quiz variables: points, number
		right, and tries.
		"""
		while True:
			if self.is_answer_correct():
				status = 'Correct! +10 points!'
				self.answer_label.config(text=status, font='Helvetica 14 bold', fg='#ffbb00')
				self.points = self.points + 10 # add 10 points to score
				self.num_right = self.num_right + 1 # add num_right score
				stop_asking = False
				self.tries = 2 # 2 tries
				break
			else:
				status = 'Incorrect! -5 points! You have 1 more try.'
				self.points = self.points - 5 # lose 5 points from score
				self.answer_label.config(text=status,font='Helvetica 14 bold', fg='#ffbb00')
				self.tries = self.tries - 1 # lose a try
				if self.tries == 0: # when no tries left
					status = 'Incorrect! -5 points! No tries left.'
					status += ' The correct answer is: {}'.format(self.get_current_answer()) # show correct answer
					self.answer_label.config(text=status, fg='#ffbb00', font='Helvetica 14 bold')
					self.points = self.points - 5 # lose 5 points from score
					stop_asking = True 
					self.tries = 2 # reset tries back to 2
					break
			
			if stop_asking:
				self.tries = 2 # reset tries back to 2
				break
			
	def _update_questions_remaining(self):
		"""
		Holder function that continues running through the quiz if all of the questions have not been gone through yet.
		"""
		pass

	def _update_question(self,question):
		"""
		Function that updates the question label shown to the next one in the set.

		Args:
			question: string for the question
		"""
		self.questions_label.config(text=question)

	def get_next_question(self):
		'''
		Function that gets the next question in the set and responds by showing quiz stats if there are no more questions left.
		'''
		self.current_question_index += 1 # adds 1 to question index
		if self.current_question_index == len(self.questions):# if last question has been answered
			self.questions_box.grid_forget() # hide questions box
			self.my_progress.grid_forget() # hide progress bar
			self.study_again_button.grid(row=2, column=1) # show study again button
			tk.Label(self.root, text="Congratulations - you finished the quiz! ",font='Helvetica 16 bold', bg='#375e97', fg='#ffbb00').grid(row=3) # show questions correct
			tk.Label(self.root, text=str(self.num_right) + " " + "out of" + " " + str(self.number_of_questions) + " " + "questions were answered correctly.",font='Helvetica 16 bold', bg='#375e97', fg='white').grid(row=4)
			tk.Label(self.root, text="Total number of points:" + " " + str(self.points) + " " + "out of" + " " + str(self.points_possible),font='Helvetica 16 bold', bg='#375e97', fg='white').grid(row=5) #show total points
			return
		else:
			self._update_questions_remaining() # continue going through questions
		self._update_question(self.get_question())
		self._update_options(self.get_options())

	def check_and_update(self):
		"""
		Function updates the answer label showon to incorrect/correct based on whether the user answered correctly. After a set 
		time, the function will update to get the next question in the set.
		"""
		self._update_answer_label()
		self.root.after(1500,self.get_next_question) # time delay between questions

	def _make_options(self,options_list):
		"""
		Function that makes the GUI radio buttons for the question answer options.

		Args:
			options_list: list of options for the question
		"""
		for option,index in zip(options_list,range(len(options_list))):
			self.option_buttons.append(tk.Radiobutton(self.questions_box, text=option, font='Helvetica 16', bg='#375e97',fg='white', value=index+1, variable=self.user_answer))
			self.option_buttons[-1].grid(row=index+1)

	def _update_options(self,options_list):
		"""
		Function that updates the option choices shown to the ones for the next question in the set.

		Args:
			options_list: list of options for the question
		"""
		self.user_answer.set(7)
		for option_button,option,index in zip(self.option_buttons,options_list,range(len(options_list))):
			option_button.config(text=option, value=index+1)
	
	def clock(self):
		"""
		Function that creates and displays a clock showing current time in Hour:Minute:Seconds:PM/AM.
		"""
		self.hour = time.strftime("%I") # hour
		self.minute = time.strftime("%M") # minute
		self.second = time.strftime("%S") # second
		self.am_pm = time.strftime("%p") # am/pm

		self.clock_label = tk.Label(self.root, text="", font='Helvetica 16 bold', fg="black", bg="#ffbb00")
		self.clock_label.grid(row=0, column=0, padx=20)
		self.clock_label.config(text=self.hour + ":" + self.minute + ":" +self.second + " " + self.am_pm)
		self.clock_label.after(1000, self.clock) # time delay to update clock

	def _build_gui(self):
		"""
		Function that builds primary GUI components of application.
		"""
		# main screen set-up
		self.root = tk.Tk()  # create a Tk window object, call it root
		self.root.geometry('600x300') # window size
		self.root.title("StudyStar⭐️") # window title
		self.root.configure(background = '#375e97') # set background color
		self.welcome_label = tk.Label(self.root, text="StudyStar⭐️", font='Helvetica 18 bold', bg='#375e97', fg='white').grid(row=1, column=0, padx=20)
		self.user_answer = tk.IntVar()
		
		# choose .csv file set-up
		self.qset_name_label = tk.Label(self.root, text="Click to choose a .csv file:",font='Helvetica 14 bold', bg='#375e97', fg='white')
		self.qset_name_label.grid(row=3, pady=40)
		self.qset_name_button = Button(self.root, text="Load File and Start Quiz", font='Helvetica 16', fg='#3f681c', highlightbackground='#375e97', command=lambda:[self.browse_files(), self.start()]) 
		self.qset_name_button.grid(row=3, column=1, columnspan=1)
		
		# set-up questions
		self.questions_box = tk.Frame(self.root, bg='#375e97') # questions/answers/answer label
		self.questions_label = tk.Label(self.questions_box, bg='#375e97',fg='#ffbb00', font='Helvetica 20 bold')
		self.questions_label.grid(row=0)
		
		# set-up answers
		self.option_buttons = [] # list of option buttons
		self.answer_label = tk.Label(self.questions_box, bg='#375e97')
		self.answer_label.grid(row=5)

		## set-up buttons ##
		# submit button
		self.submit_button = tk.Button(self.questions_box, text="Check Answer", font='Helvetica 16 bold', fg='#3f681c', highlightbackground='#375e97', command=lambda:[self.check_and_update(), self.step()])

		# start quiz button
		self.side_box = tk.Frame(self.root, bg='#375e97')

		# quit quiz button
		self.quit_button = tk.Button(self.root, text="Quit Quiz", font='Helvetica 16', fg='red', highlightbackground='#375e97', command=self.root.quit)
		self.quit_button.grid(row=0, column= 1)

		# about quiz button
		self.about_button = tk.Button(self.root, text="Instructions", font='Helvetica 16', highlightbackground='#375e97', command=self.about)
		self.about_button.grid(row=1, column=1)

		# study again button
		self.study_again_button = tk.Button(self.root, text="Study Again",font='Helvetica 16', fg='#3f681c', highlightbackground='#375e97', command=None) #TODO
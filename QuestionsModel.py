#-------------------------------------------------------------------------------
# Name:      QuestionsModel.py
# Purpose:   Program flow for reading the questions set .csv files
# Author(s): Brittni Wendling
# Created:   06/09/2020
# Updated:   08/07/2020
#-------------------------------------------------------------------------------

"""
This module serves as the program flow for reading the questions set .csv files.
It is used in the main.py file.
"""

# import the required modules
import csv
import random

def get_questions(filename):
	"""
	A function that reads from a selected .csv file and creates list of question objects.

	Args:
		filename: the .csv file a user chooses via the GUI's filedialog selector

	Returns:
		questions: list of contents for each question row

	Raises:
		prints an error "unable to process request" if reading .csv file is unsuccessful
	"""
	questions = None
	try:
		with open(filename,'r') as file: # open .csv file
			reader = csv.reader(file) # create reader object, read .csv file
			next(reader, None)  # skip the headers
			questions = list(reader) # list of contents for each row
			lines = len(questions) # number of questions
			random.shuffle(questions) # shuffle question order
	except:
		print("unable to process request")

	return questions
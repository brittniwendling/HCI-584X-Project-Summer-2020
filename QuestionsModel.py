#-------------------------------------------------------------------------------
# Name:      QuestionsModel.py
# Purpose:   Primary program flow for StudyStar⭐️ Quiz Application
# Author(s): Brittni Wendling
# Created:   06/09/2020
# Updated:   08/07/2020
#-------------------------------------------------------------------------------

'''reads from a file '''

# read/write from/to a file.

# import the required modules
import csv
import random

def get_questions(filename):
	'''reads from a file and creates list of question objects'''
	questions = None
	try:
		with open(filename,'r') as file:
			reader = csv.reader(file)
			next(reader, None)  # skip the headers
			questions = list(reader)
			lines = len(questions)
			random.shuffle(questions) # shuffle question order
	except:
		print("unable to process request")

	return questions
#-------------------------------------------------------------------------------
# Name:      main.py
# Purpose:   Main program for running the StudyStar⭐️ Quiz Application
# Author(s): Brittni Wendling
# Created:   06/09/2020
# Updated:   08/07/2020
#-------------------------------------------------------------------------------

'''Main file - run this!
This is a data-driven TKinter quiz application written in Python 3.7. The purpose of StudyStar⭐️ is to
allow users to create their own question sets via .csv files. The question sets .csv files are run through
the app and presented back to users in order to quiz themselves on the content. 
github repo: https://github.com/brittniwendling/HCI-584X-Project-Summer-2020 ''' 

from CreateQuizApp import *

print("Welcome to StudyStar⭐️, a study-based quiz application created by Brittni Wendling in Summer 2020.")

# create an app instance of the MainQuizApp class to begin the program
app = MainQuizApp()


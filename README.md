# StudyStar ⭐️ ReadMe (User’s guide)
This is a data-driven TKinter quiz application written in Python 3.7. The purpose of StudyStar⭐️ is to allow users to create their own question set .csv files and have a way to have the sets presented back to them in order to quiz themselves on the content. This prevents the need of using physical flashcards or things of that nature that require a lot of manual effort. The target users for StudyStar are students, professionals, and anyone who needs a resource for studying to reinforce learning material. 

Here are the project file/folder structures:
main.py: imports from the stuff module (the local stuff.py file)
run_testpak.py: uses a simple package (called testpak) that can be installed via pip.

# Requirements
In order to run the program, it is recommended to have Python 3.7. All of the packages in this project are part of the Python Standard Library and should not require separate installations. Here is a list of the Python Standard Library packages and modules used:
tkinter
datetime
time
csv
random

# Installation
List what the user needs to do before running your app
for main.py
use pip to install the required third party packages:  pip -r requirements.txt
for run_testpak.py
use pip to build and install testpack as a local package and install required packages
open a OS terminal, go into the project root folder and type: pip install . (<- dot!)

# Usage
Describe how to run your app
main.py: run it in the project root folder, so it can import from the testpack folder
testpak.py: can be run from any folder once it’s been installed locally
After creating .csv files storing question sets, StudyStar allows users to select which .csv file they would like to run through the application. The application will populate with the selected .csv file with the appropriate questions and answers. 
The alternative is to have the user start your app via a
​
command line interface
(CLI)
​
using a terminal.
●
The user still needs to clone your project and be able to "jump" into that folder in
the command line. They also need to have all prerequisites installed! They would
open a OS terminal (cmd.exe or PowerShell on Windows, terminal on Mac), use
cd to jump to the project root folder (e.g.
​
cd
/Users/chris/Desktop/MyCoolApp
​
) and give your main.py to a python
interpreter:
​
python main.py
●
This would be the equivalent of you hitting Run with main.py in your IDE and any
print() and input() would happen via the OS terminal.


1. Download quizapp.py and the CSV files.
2. Run quizapp.py. Make sure you have write access to the directory this is run from!
3. The app will automatically create `quizapp.sqlite` using the CSV files and seed it with fake player scores.
4. Answer questions. When a question has multiple correct answers, your response can be separated any way you please; the script doesn't differentiate between `A, B` or `ba`.

# Code Examples
If your project code is meant to be integrated into python code, you should list at least a few usage examples that can be copy/pasted and run. For more complex cases, consider writing a separate tutorial (put it and its code into a separate folder called tutorial).
Here, I’ll just give one of the functions that my package defines:
# use the evenOdd function
from testpak import evenOdd
x = int(input("Enter a number:"))
print(x, "is",  evenOdd(x))

# Known issues
List any known bugs and limitations

# Acknowledgments
Thanks to Dr. Chris Harding, Iowa State University, for his teaching, guidance, and assistance with this project. 


Welcome to StudyStar⭐️ - an app for all your studying needs! To begin studying, please click the “Load 
File and Start Quiz” button. This button will open up a file selector where you can choose any .csv file to fun through the app. Please see the ReadMe.md for full information on how the file will need to be structured in order to work properly with the app.

After you choose your .csv file to load, StudyStar⭐️  will automatically begin the quiz. One questions will be shown at a time, where you will choose your answer and click the “Check Answer” button. You will then be provided with feedback on whether your answer was correct. A progress bar is shown at the bottom of the quiz, which shows you real-time feedback of your progress towards finishing the quiz. Once you answer all of the questions, you will be shown how many questions you got right and your total score! Exit the quiz at any point by clicking the “Quit Quiz” button in the top right corner.





Example of a project ReadMe (User's guide)

Start with a simple description of what your project does. This here gives examples of 2 simple project file/folder structures:

main.py: imports from the stuff module (the local stuff.py file)
run_testpak.py: uses a simple package (called testpak) that can be installed via pip.
HCI584X_Project-LIFE

Learning Important Factual Equivalents (Calorie Edition) - Python A small test app that translates common fast food menu items (that a User selects) to equivalent physical exercise duration/exertion level and healthy alternatives that people can more easily relate with. This information is meant to educate and entertain by helping the user understand the equivalent effort to offset consumption (provided the consumption is in excess of the minimum amount of calories for normal exertion throughout the day) as well as to share findings through messaging/social media in a consumable format a "Meme Card".

Requirements

Python 3.7 or higher
rich
dill 0.3 or higher
Installation

List what the user needs to do before running your app for main.py

use pip to install the required third party packages: pip -r requirements.txt
Pillow==7.0.0

for run_testpak.py

use pip to build and install testpack as a local package and install required packages
open a OS terminal, go into the project root folder and type: pip install . (<- dot!)
Usage

Describe how to run your app

main.py: run it in the project root folder, so it can import from the testpack folder
testpak.py: can be run from any folder once it's been installed locally
Code Examples

If your project code is meant to be integrated into python code, you should list at least a few usage examples that can be copy/pasted and run. For more complex cases, consider writing a separate tutorial (put it and its code into a separate folder called tutorial). Here, I'll just give one of the functions that my package defines:

# use the evenOdd function
from testpak import evenOdd
x = int(input("Enter a number:"))
print(x, "is",  evenOdd(x))
Known issues

List any known bugs and limitations

Acknowledgments

If some project was instrumental in helping you with this project, consider listing it here.

How to markdown?

see https://guides.github.com/features/mastering-markdown/ for a guide on markdown.

Note that images need to be referenced, i.e. you will need to put them into a separate folder, here I've put an image into my docs folder:

Alt text for image

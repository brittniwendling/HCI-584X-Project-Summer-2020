# StudyStar ⭐️ ReadMe (User’s guide)
Welcome to StudyStar⭐️ - an app for all your studying needs! This is a data-driven TKinter quiz application written in Python 3.7. The purpose of StudyStar⭐️ is to allow users to create their own question set .csv files and have a way to have the sets presented back to them in order to quiz themselves on the content. This prevents the need of using physical flashcards or things of that nature that require a lot of manual effort. The target users for StudyStar are students, professionals, and anyone who needs a resource for studying to reinforce learning material. 

Here are the project file/folder structures:

- main.py: main program for running the StudyStar⭐️Quiz Application. Imports from the QuestionsModel and CreateQuizApp module 
- CreateQuizApp.py: primary program flow for StudyStar⭐️Quiz Application
- QuestionsModel.py: reads from a .csv file a user selects and creates list of question objects to run through the app
- questions csv files folder: folder that includes 3 examples of .csv question set files, as well as a place for users to save their created .csv question sets

# Requirements
In order to run the program, it is recommended to have Python 3.7. All of the packages in this project are part of the Python Standard Library and should not require separate installations. Here is a list of the Python Standard Library packages and modules used:

1. tkinter
2. datetime
3. time
4. csv
5. random

# Installation
No additional packages are required on install.

# Usage
First, clone the project file.
main.py: run in the project root folder. Open an OSterminal, use cd to jump to the project root folder, and give main.py to a python interpreter: "python main.py", so it can import from QuestionsModel.py and CreateQuizApp.py.

To begin using StudyStar⭐️, users will need to have previously created .csv files storing question sets prior to starting the application. The structuring requirements for these .csv files to work properly with the application are described below. To see an example of what this structuring looks like, please see the 3 .csv file exmaples located in the "questions csv files" folder in the root project folder. You are encouraged to save the .csv files you create in this folder as well.

.csv file structuring guidelines: 
1. Have the first row of the .csv file be a header row with the names "Question", "Choice 1", Choice 2", Choice 3", Choice 4", "Correct Answer". Although it is technically possible to have more than 4 "Choice" options, it is not recommended, due to keeping the GUI clean and quiz clean from complications.
2. Type your questions in the "Question" column. The app will use this column to present this back as the question while taking the quiz. You can type them in whatever formatting/wording works best for you. Some examples:The unit of charge is called the _____.;The symbol Mn on the periodic table stands for:;100 + 100 = ?; Who founded Apple?
3. Type your question answer options in the "Choice" columns. The app will use these columns to present the content back in radio buttons displaying answers to choose from while taking the quiz.
4. Type the correct answer out of the options in the "Correct Answer" column. The "Correct Answer" column designates the correct answer and is what the application uses to know if the user selected an answer correctly or incorrectly. 
5. Save your .csv file anywhere on your computer (not required, but recommended to save all files in in the actual project root folder called "questions csv files") with a name that describes the study question set, such as "science_exam7", "math_quiz2", "english_test1", etc.

### NOTE: You can add as many questions to the .csv file as you like. The app will run through however many are in the file, whether that number be 5, 50, 100, etc. ###

To start studying, please click the “Load File and Start Quiz” button. This button will open up a file selector where you can choose any .csv file you created (structured as described in the previous steps) to fun through the app. StudyStar⭐️ allows users to select which .csv file they would like to run through the application. The application will populate with the selected .csv file with the appropriate questions and answers.

After choosing your .csv file to load, StudyStar⭐️ will automatically begin the quiz. One questions will be shown at a time, where you will choose your answer and click the “Check Answer” button. You will then be provided with feedback on whether your answer was correct. A progress bar is shown at the bottom of the quiz, which shows you real-time feedback of your progress towards finishing the quiz. Once you answer all of the questions, you will be shown how many questions you got right and your total score! Exit the quiz at any point by clicking the “Quit Quiz” button in the top right corner.

# Known issues
As of 08/07/20, there are no known bugs.

# Acknowledgments
Thanks to Dr. Chris Harding, Iowa State University, for his teaching and guidance with this project. 



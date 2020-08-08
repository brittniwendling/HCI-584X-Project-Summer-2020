import random # imports random module

# set name of question set
def set_qset_name():
    qset_name = input("Please enter a name for your question set and hit Enter:")
    print("Your questions set is called:", qset_name)
    
set_qset_name()

# Create dictionary of questions and answers
# hardcoded for now; change to input later
questions = {
            'Who is president of USA?':
            ('\na. Clinton\nb. Oprah\nc. Obama\nd. Trump\n', 'd'),
            'What is the capital of USA?':
            ('\na. Iowa\nb. New York\nc. Washington\nd. Seattle', 'c'),
            'What color is the sun?':
            ('\na. Yellow\nb. Blue\nc. Green\nd. White\n', 'a'),
            'What is 10 - 4?':
            ('\na. 0\nb. 6\nc. 2\nd. 19\n', 'b'),
            'What is 5 + 0?':
            ('\na. 5\nb. 7\nc. 4\nd. 2\n', 'a'),
            }

# asks random questions from questions dictionary
def ask_question(questions):
    '''Asks random question from 'questions' dictionary and returns
       players' attempt and correct answer.'''

    item = random.choice(list(questions.items()))
    question = item[0]
    (variants, answer) = item[1]
    print(question, variants)
    attempt = input('\nHit \'a\', \'b\', \'c\' or \'d\' and Enter for your answer\n')
    return (attempt, answer)

# Questions loop
tries = 3
score = 0
for questions_number in range(10):
    while True: # Asking 1 question at a time
        attempt, answer = ask_question(questions)
        if attempt not in {'a', 'b', 'c', 'd'}:
            print('INVALID INPUT! Only hit \'a\', \'b\', \'c\' or \'d\' for your response')
            print('YOUR CURRENT SCORE IS:', score)
        elif attempt == answer:
            print('CORRECT! Nice work!')
            score = score + 10 # add 10 points
            print('YOUR CURRENT SCORE IS:', score)
            stop_asking = False
            break
        elif tries == 0: # Specify the number of tries to fail the answer        
            print('INCORRECT! You ran out of your attempts')
            score = score - 5 #lose 5 points
            print('YOUR CURRENT SCORE IS:', score)
            stop_asking = True
            break
        else:
            tries = tries - 1
            print('INCORRECT! Try again.')
            score = score - 5 #lose 5 points
            print('YOUR CURRENT SCORE IS:', score)
    if stop_asking:
        break

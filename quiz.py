#quiz
from questions import quiz

score = 0
attempts = 0

#Check answers to see if they are correct or not
def checkAnswer(question, answer, score, attempts):
    if quiz[question]['answer'].lower == answer.lower:
        print("Correct answer! Your score is ",(score + 1))
        return True
    else:
        print("Incorrect answer! You have", attempts,"remaining.")
        return False 

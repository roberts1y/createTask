#quiz
from questions import quiz

score = 0

#Check answers to see if they are correct or not
def checkAnswer(question, answer, score, attempts):
    if quiz[question]['answer'].lower == answer.lower:
        print("Correct answer! Your score is ",(score + 1))
        return True
    else:
        print("Incorrect answer! You have", attempts,"remaining.")
        return False 

while True:
    for question in quiz:
        attempts = 3
        while attempts > 0:
            print(quiz[question]['question'])
            answer = input("Enter your answer, to skip the question type 'skip' :")
            if answer.lower == "skip":
                break
            check = checkAnswer(question, answer, score, attempts)
            if check == True:
                score += 1
                break
            attempts -= 1



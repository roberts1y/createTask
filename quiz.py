#quiz
from questions import quiz

score = 0

print('')
print("Welcome to my game! Answer the trivia question with the correct answer to earn a point. Try repeating the game as many times you want to score the maximum amount of points. Good luck!")
print('')

#Check answers to see if they are correct or not
def checkAnswer(question, answer, score, attempts):
    if quiz[question]['answer'] == answer:
        print("Correct answer! Your score is ",(score + 1))
        print('')
        return True
    else:
        print("Incorrect answer! You have", attempts,"attempts remaining.")
        print('')
        return False 

while True:
    for question in quiz:
        attempts = 3
        while attempts > 0:
            print(quiz[question]['question'])
            answer = input("Enter the answer, if you don't know the answer or would like to move on to the next question, type 'skip' : ")
            attempts = attempts - 1
            if answer == "skip":
                print('')
                break
            check = checkAnswer(question, answer, score, attempts)
            if check:
                score = score + 1
                break
    break

print("Your final score is", score)
print("Thanks for playing!")
            


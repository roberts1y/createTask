#quiz
from questions import quiz

score = 0

print('')
print("""Welcome to my game! Answer the trivia question with the correct answer to earn a point. 
Try repeating the game as many times you want to score the maximum amount of points. Good luck!""")
print('')



#Check answers to see if they are correct or not
def checkAnswer(question, answer, score, attempts):
    if quiz[question]['answer'].lower() == answer.lower():
        print("Correct answer! Your score is ",(score + 1))
        print('')
        return True
    if attempts == 0:
        print("Awww, sorry! You're all out of attempts :(. The correct answer was", quiz[question]['answer']+".")
        print("")
        return False
    else:
        print("Incorrect answer! You have", attempts,"attempts remaining.")
        print('')
        return False 


while True:
    start = input("When you're ready to start, type anything and press enter : ")
    print("")
    if start:
        for question in quiz:
            attempts = 3
            while attempts > 0:
                print(quiz[question]['question'])
                answer = input("Enter the answer, if you don't know the answer or would like to move on to the next question, type 'skip' : ")
                attempts -= 1
                if answer.lower() == "skip":
                    print("The correct answer was", quiz[question]['answer']+".")
                    print('')
                    break
                check = checkAnswer(question, answer, score, attempts)
                if check:
                    score += 1
                    break
        break


print("Your final score is", score)
if score < 6:
    print("Not bad, but you only scored",score,"maybe you could do a little better next time...")
if 10 > score >= 6:
    print("Wow, you scored",score,"points! You're a pro. Great job!")
if score == 10: 
    print("Jeez, you must be cheating! You scored",score,"points.")
print("Thanks for playing!")
            


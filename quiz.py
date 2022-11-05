#quiz
#imports my dictionary
from questions import quiz

score = 0

#simple intro message
print('')
print("""Welcome to my game! Answer the trivia question with the correct answer to earn a point for a maximum of 10 
points. Try repeating the game as many times you want to score the maximum amount of points. Good luck!""")
print('')

#function which checks answers to see if they are correct or not
def checkAnswer(question, answer, score, attempts):
    #checks a question's corresponding lowercase answer with the user's lowercase 
    if quiz[question]['answer'].lower() == answer.lower():
        print("Correct answer! Your score is",(score + 1))
        print('')
        return True
    #checks to see if user is out of attempts and if so will trigger the next question
    if attempts == 0:
        print("Awww, sorry! You're all out of attempts :(. The correct answer was", quiz[question]['answer']+".")
        print("")
        return False
    #anything besides 'skip' or the correct answer is considered incorrect so I use an else statement here
    else:
        print("Incorrect answer! You have", attempts,"attempts remaining.")
        print('')
        return False 

#while statement continues to run until all questions have been answered
while True:
    #input which allows user to read instructions before typing anything and making the start 'if' statement true
    start = input("Remember, when taking the quiz capitalization does NOT matter. When you're ready to start, type anything and press enter : ")
    print("")
    if start:
        #goes through every question in 'quiz' which is my dictionary
        for question in quiz:
            attempts = 3
            while attempts > 0:
                #prints question and continues to print each question after the question prior is answered
                print(quiz[question]['question'])
                #asks user to input an answer
                answer = input("Enter the answer, if you don't know the answer or would like to move on to the next question, type 'skip' : ")
                attempts -= 1
                #prints the correct answer if user skips
                if answer.lower() == "skip":
                    print("The correct answer was", quiz[question]['answer']+".")
                    print('')
                    break
                #calls the checkAnswer procedure and checks the answer
                check = checkAnswer(question, answer, score, attempts)
                #if answer is correct returns true, increases score, and moves on to the next question
                if check:
                    score += 1
                    break
        break

#prints the final score
print("Your final score is", score)
#some simple 'if' statements for funny finishing phrases
if score < 6:
    print("Not bad, but you only scored",score,"maybe you could do a little better next time...")
if 10 > score >= 6:
    print("Wow, you scored",score,"points! Great job!")
if score == 10: 
    print("Jeez, you must be cheating! You scored",score,"points. That's every question right!")
print("Thanks for playing!")
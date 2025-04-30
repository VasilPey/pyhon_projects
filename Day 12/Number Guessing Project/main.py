import random
from art import logo
lives = 10
game_on = True
def check_guesses(number,r_number):
    global game_on
    if number > r_number:
        print("Too high.")
    elif number < r_number:
        print("Too low.")
    elif number == r_number:
        print("You guessed it!")
        game_on = False


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
random_number= random.randint(1,100)
user_difficulty=input("Choose a difficulty.Type 'easy' or 'hard':").lower()
if (user_difficulty == "easy"):
    lives = 10
elif (user_difficulty == "hard"):
    lives = 5
else:
    print("There isn't such difficulty.Setting the difficulty on easy by default")
    lives = 10
while game_on:
    print(f"You have {lives} attempts remaining to guess the number.")
    try:
        user_guess = int(input("Make a guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    if lives == 1 and user_guess != random_number:
        print(f"You've run out of guesses.\nThe number was {random_number}.\nRefresh the page to run again")
        game_on = False
    else:
        check_guesses(user_guess, random_number)
        if(game_on == True):
            lives -= 1


















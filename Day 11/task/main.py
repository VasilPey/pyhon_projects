import random
from art import logo
ace = 11
cards = [ace,2,3,4,5,6,7,8,9,10,10,10,10]
def has_blackjack(user_cards,computer_cards):
    if (user_cards[0] == ace and user_cards[1] == 10):
        print("You win!")
        return
    elif (user_cards[0] == 10 and user_cards[1] == ace):
        print("You win")
        return
    if (computer_cards[0] == ace and computer_cards[1] == 10):
        print("You lose!")
        return
    elif (computer_cards[0] == 10 and computer_cards[1] == ace):
        print("You lose")
        return
def who_wins(user_score,computer_score):
    if user_score > 21:
        print("You went over.You lose")
    elif computer_score > 21:
        print("You win!")
    elif user_score > computer_score:
        print("You win!")
    elif computer_score > user_score:
        print("You lose!")
    else:
        print("Draw")

user_playing = input("Do you want to play a game of Blackjack?Type 'y' or 'n':".lower())
while user_playing == "y":
    print(logo  )
    user_cards = random.sample(cards,2)
    computer_cards = random.sample(cards,2)
    user_score = (user_cards[0] + user_cards[1])
    print(f"Your cards:  {user_cards}, current score: {user_score}")
    if (user_score > 21):
        if ace in user_cards:
            user_cards[user_cards.index(ace)] = 1
            user_score = sum(user_cards)
            if user_score > 21:
                print("You lose")
    print(f"Computers first card: {computer_cards[0]}")
    user_choice = input("Type 'y' to get another card, type 'n' to pass:\n".lower())
    computer_score = (computer_cards[0] + computer_cards[1])
    if user_choice == "y":
        while user_choice == "y":
            new_card = random.choice(cards)
            user_cards.append(new_card)
            user_score = sum(user_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")
            if user_score > 21:
                break
            user_choice = input("Type 'y' to get another card, type 'n' to pass:\n".lower())

    elif user_choice == "n":
        while computer_score < 17:
            new_card = random.choice(cards)
            computer_cards.append(new_card)
            computer_score = sum(computer_cards)
    print(f"Your final hand is: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    has_blackjack(user_cards,computer_cards)
    who_wins(user_score,computer_score)
    user_playing = input("Do you want to play a game of Blackjack?Type 'y' or 'n':".lower())





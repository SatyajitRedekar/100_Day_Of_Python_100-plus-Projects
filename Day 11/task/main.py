import art
import random
from os import system

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
human_cards = []
computer_cards = []

flag = True

# todo : how long game will go
def play_game() :
    global flag
    play = input("Do yo want to play the Game press 'y' or 'n' : ").lower()
    if play == "y":
        flag = True
        return
    elif play == "n":
        flag = False
        play_game()
    else:
        print("invalid choice ! ")
        play_game()

def reinsert_computer_card() :
    global flag
    global computer_cards_score
    print("Computer geting a card : ")
    holder = random.choice(cards)
    computer_cards.append(holder)
    computer_cards_score = sum(computer_cards)

    print(f"\tYour cards : {human_cards} , current score : {human_cards_score} ")
    print(f"\tComputer's cards : {computer_cards} , current score : {computer_cards_score}")

    if computer_cards_score > 21:
        print("You won ")
        play_game()
    elif computer_cards_score < 16:
        reinsert_computer_card()
    else:
        return

def find_winner() :
    global computer_cards_score
    global human_cards_score
    if computer_cards_score > 21 :
        if 11 in computer_cards :
            computer_cards_score -= 11
            computer_cards_score += 1

    if human_cards_score > 21 :
        if 11 in human_cards :
            human_cards_score -= 11
            human_cards_score += 1

    if human_cards_score > 21:
        # print(f"\tYour cards : {human_cards} , current score : {human_cards_score} ")
        # print(f"\tComputer's cards : {computer_cards} , current score : {computer_cards_score}")

        print("\tYou lost !")
        play_game()

    elif computer_cards_score < 16 :
       reinsert_computer_card()
    elif computer_cards_score == human_cards_score :
        print("Match draw !")
        play_game()

    if computer_cards_score > human_cards_score :
        # print(f"\tYour cards : {human_cards} , current score : {human_cards_score} ")
        # print(f"\tComputer's cards : {computer_cards} , current score : {computer_cards_score}")

        print("you lost !")
        play_game()
    else:
        # print(f"\tYour cards : {human_cards} , current score : {human_cards_score} ")
        # print(f"\tComputer's cards : {computer_cards} , current score : {computer_cards_score}")

        print("you won !")
        play_game()

def reinsert_card() :
    global human_cards_score
    # TODO 2 : do you want to add the cards
    other_card = input("Do you want other card 'y' or 'n' : ").lower()
    if other_card == "y":
        holder = random.choice(cards)
        human_cards.append(holder)
        human_cards_score = sum(human_cards)

        print(f"\tYour cards : {human_cards} , current score : {human_cards_score} ")
        print(f"\tComputer's First card : {computer_cards[0]}")

        # TODO 3 : bust rules
        if human_cards_score == 21 :
            print(f"\tComputer's cards : {computer_cards} , current score : {computer_cards_score}")
            print("you won !")
        if human_cards_score > 21:
            print(f"\tComputer's cards : {computer_cards} , current score : {computer_cards_score}")
            print("\tYou lost !")
        elif human_cards_score < 21:
            reinsert_card()
    elif other_card == "n" :
        print(f"\tYour cards : {human_cards} , current score : {human_cards_score} ")
        print(f"\tComputer's cards : {computer_cards} , current score : {computer_cards_score}")
        find_winner()
    else:
        print("invalid choice !")
        reinsert_card()

while flag :
    play_game()
    system("cls")
    print(art.logo)

    # TODO 1 : fist round
    human_cards = random.choices(cards,k=2)
    computer_cards = random.choices(cards,k=2)
    human_cards_score = sum(human_cards)
    computer_cards_score = sum(computer_cards)
    print(f"\tYour cards : {human_cards} , current score : {human_cards_score} ")
    print(f"\tComputer's First card : {computer_cards[0]}")

    if human_cards_score == 21 :
        print(f"\tYour cards : {human_cards} , current score : {human_cards_score} ")
        print(f"\tComputer's cards : {computer_cards} , current score : {computer_cards_score}")

        print("You won this game !")
        play_game()

    reinsert_card()
import art
from random import randint
from os import system

print(art.logo + "\n")
welcome = "\twelcome to the Guessing game"
live = 1

def play_again() :
    again = input("If you want to play again then type y or n : ").lower()
    if again == "y" :
        guess_game()
    else:
        exit()

# TODO 1 : repeat the game
def guess_game() :
    global live
    while live >= 0 :

        print("I am thinking number between 1 to 100 ")
        number = randint(1,100)
        print(f"the number is {number}")

        difficulty = str(input("choose the difficulty type easy, medium , hard : ")).lower()
        if difficulty == "hard" :
            live = 5
        elif difficulty == "medium" :
            live = 7
        else:
            live = 10

        print(f"You have {live} attempts remaining to guess the number.")

        def game_play() :
            global live
            if live == 0 :
                print("\tYou lost !")
                play_again()

            guess = int(input("Make guess : "))
            if guess == number :
                print("\tyou got the number you won !")
                play_again()
            elif guess > number :
                print("Too high...")
                live -= 1
                print(f"You have {live} attempts remaining to guess the number.")
                game_play()
            elif guess < number :
                print("Too low...")
                live -= 1
                print(f"You have {live} attempts remaining to guess the number.")
                game_play()

        game_play()

print(welcome.title())
system("cls")
guess_game()
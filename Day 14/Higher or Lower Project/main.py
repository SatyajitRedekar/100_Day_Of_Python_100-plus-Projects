import random
from game_data import data
from art import logo,vs

print(logo)
score = 0

# TODO 2 : show score if score is > 0
def show_score() :
     print(f"sorry, that's wrong your score is : {score}")

# TODO 3 : show first compaired info
while True :
    a = random.choice(data)
    count_of_a= a["follower_count"]
    print(f"compair A :{a["name"]} ,{a["description"]},{a["country"]} ")

    # TODO 4 : show the logo of vs

    print(vs)

    # TODO 5 : next compired name and info

    b = random.choice(data)
    count_of_b= b["follower_count"]
    print(f"against B :{b["name"]} ,{b["description"]},{b["country"]} ")

    # TODO 6 : result of comparsion and update score

    ans = str(input("Who has more followers ? Type A or B : ")).lower()
    if ans == "a" :
        if count_of_a > count_of_b :
            print("you are correct !")
            score += 1
            show_score()
        else:
            print("you are wrong !")
            show_score()
            break
    elif ans == "b" :
        if count_of_a < count_of_b :
            print("you are correct !")
            score += 1
            show_score()
        else:
            print("you are wrong !")
            show_score()
            break
    else:
        show_score()
        break
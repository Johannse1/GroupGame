# group: Evan Johanns, Luis Martinez
# Dice Game
# 10/31/19

import random


def roll():
    num = random.randint(1,6)
    return num


def play_game():
    wins = []
    p1_points = 0
    p2_points = 0
    while p1_points != 5 and p2_points != 5:
        player_one = roll()
        player_two = roll()

        print(f"player ones roll: {player_one}")
        print(f"player twos roll: {player_two}")
        print(f"player ones points: {p1_points}")
        print(f"player twos points: {p2_points}")
        if player_one > player_two:
            print(f"player one wins with a roll of {player_one}.")
            p1_points = p1_points + 1

        elif player_one == player_two:
            print("same roll.")

        else:
            print(f"player two wins with a roll of {player_two}.")
            p2_points = p2_points + 1
        input("press enter to roll again: ")

    if p1_points == 5:
        print("Player one Wins!")
        wins.append("player one")

    elif p2_points == 5:
        print("Player two Wins!")
        wins.append("player two")

    # luis - right here should be code that shows how many wins each player has
    # take them from the list that i created at the top


play_game()

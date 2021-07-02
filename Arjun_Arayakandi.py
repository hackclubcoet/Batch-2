#Arjun Arayakandi-2-stone paper scissors
import random

player_action = input("Enter a choice (rock, paper, scissors): ")
actions = ["rock", "paper", "scissors"]
computer_action = random.choice(actions)
print("\nYou chose {}, computer chose {}.\n".format(player_actio,computer_action) )

if player_action == computer_action:
    print("Both players selected {}. It's a tie ".format(player_action))
elif player_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win")
    else:
        print("Paper covers rock! computer wins")
elif player_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win")
    else:
        print("Scissors cuts paper! computer wins")
elif player_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win")
    else:
        print("Rock smashes scissors! computer wins")

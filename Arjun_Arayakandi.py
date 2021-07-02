# Arjun Arayakandi-2-stone paper scissors

import random  # importing random characters

player_action = input("Enter a choice (rock, paper, scissors): ")  # making the player choose one
actions = ["rock", "paper", "scissors"]
computer_action = random.choice(actions)  # making the computer choose one
print("\nYou chose {}, computer chose {}.\n".format(player_action, computer_action))  # printing the chosen ones

# if the player and the computer choose the same print it's a tie
if player_action == computer_action:
    print("Both players selected {}. It's a tie ".format(player_action))

# if the player choose rock and computer choose scissors
elif player_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win")
    # if the player choose rock and computer choose paper
    else:
        print("Paper covers rock! computer wins")

# if the player choose paper and the computer choose rock
elif player_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win")
    # if the player choose paper and computer choose scissors
    else:
        print("Scissors cuts paper! computer wins")

# if the player choose scissors and the computer choose paper
elif player_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win")
    # if the player choose scissors and the computer choose rock
    else:
        print("Rock smashes scissors! computer wins")

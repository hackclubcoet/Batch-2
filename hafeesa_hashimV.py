# Hafeesa Hashim V-batch 2-Treasure Hunt

# this is a treasure hunt game
# you are on a treasure island now!

print("Welcome to Treasure Island", "Come on lets hunt for treasure :)")
name: str = input("what is your name\n")
"""this prints your name"""
age: int = int(input("enter your age\n"))
"""this prints your age"""
if age >= 18:
    print("you are old enough to play !!")

    wants_to_play: str = input("are u ready to start\n").lower().strip()
    if wants_to_play == "yes":
        print("let's play !!")
        """for starting the game choose where to move ,it can be left or right or anything else"""
        left_or_right: str = input("first choice can be Left or right?\n")
        if left_or_right == "left":
            ans: str = input("Nice!!,you follow this path and reach the river ,Do u wanna swim across or wait there\n")
            if ans == "wait":
                """if u are waiting there you will face some doors"""
                print("you are having some coloured doors in front of you,choose")
                door = input("blue or red or yellow or any other colour\n")
                if door == "blue":
                    print("Alas! you are eaten by beast")
                    print("game over")
                elif door == "red":
                    print("Omg!!you are burned by fire")
                    print("game over")
                elif door == "yellow":
                    print("You won the treasure !!")
                else:
                    print("the door u entered is not the exact door!!")
                    print("game over")
            else:
                print("ouch!! you are attacked by trout")
                print("game over")
        else:
            print("you fell into a hole")
            print("game over")
    else:
        print("quit")
else:
    print("you are not supposed to play this game , quit")

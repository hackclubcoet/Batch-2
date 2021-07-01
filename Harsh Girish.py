import random  # Here we use random module inorder to randomly select elements
print("Hey lets roll a die !")
n = 0  # It is a variable to store the sum
p = 0  # It is a variable to store how many times did we roll the die
print("And lets add the outcome till it reaches 50 or above it.")
roll: list[int] = []
while n <= 50:  # Condition # Here we use while loop inorder to loop the and add the outcome in each roll of the die
    r = random.randrange(1, 7)  # Initialization
    roll.append(r)
    n = n + r  # Increment
    p = p + 1

print("The sum of the numbers we obtained through rolling a die is = ", n)  # Printing statement for the sum
print("The number of times we rolled the die = ", p)  # Printing statement for the roll results

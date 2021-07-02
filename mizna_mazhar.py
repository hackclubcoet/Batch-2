#Mizna_Mazhar-2-calculator
import math


def multiply(x, y):
    """this function  multiplies  x and y"""
    return x * y


def divide(x, y):
    """ this function divides y from x """
    return x / y


def add(x, y):
    """this function sums up x and y"""
    return x + y


def subtract(x, y):
    """ this funtion subtracts y from x"""
    return x - y



def sine_of_an_angle(angle):
    """ this function gives sine of an angle"""
    return math.sin(angle)


def cosine_of_an_angle(angle):
    """ this function gives cosine of an angle"""
    return math.cos(angle)


print("Please select operation:-\n"
      "1. Add\n" 
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n"
      "5. Sine\n"
      "6. Cosine\n")

choice = int(input("Select operations form 1, 2, 3, 4,5 ,6 : "))

if choice in (1, 2, 3, 4):
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
else:
    angle = int(input("please enter  an angle: "))

if choice == 1:
    print(number_1, "+", number_2, "=",
          add(number_1, number_2))

elif choice == 2:
    print(number_1, "-", number_2, "=",
          subtract(number_1, number_2))

elif choice == 3:
    print(number_1, "*", number_2, "=",
          multiply(number_1, number_2))

elif choice == 4:
    print(number_1, "/", number_2, "=",
          divide(number_1, number_2))

elif choice == 5:
    print(cosine_of_an_angle(angle))

elif choice == 6:
    print(cosine_of_an_angle(angle))

else:
    print("Invalid input")

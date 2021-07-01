#ASWANTH KV-BATCH2-Number Guessing
import random
#generating random numbers betweeen 1 to 10
n= random.randint(1,10)
#guessing the input number
guess = int(input("enter a number between 1 to 10:"))
# condition for while (wrong guess)
while n != ("guess"):
      print
      if guess < n:
         print("guess is low")
         guess = int(input("enter a number between 1 to 10:"))
      elif guess > n:
         print("guess is high")
         guess = int(input("enter a number between 1 to 10:"))
      else:
        #if guess is right
         print("you guessed it,awesome!")
         break
      

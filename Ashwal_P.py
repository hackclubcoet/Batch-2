# Ashwal P-2-Password Generator
import random  # importing random module to generate random characters

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'H', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R',
             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
             'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
             'w', 'x', 'y', 'z']  # stores Alphabets in a list
password = ''  # to store the password
print('Enter the length of the password : ')
n = int(input())  # Accepts the length of the Password
for x in range(n):  # for loop
    password = password + random.choice(alphabets)  # generates random characters and join them to form a password
print(password)  # prints the password

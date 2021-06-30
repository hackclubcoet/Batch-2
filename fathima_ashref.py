# FathimaAshref-2-HelloWorldAnimation

import time


def animation(word):
    """this function takes the input and displays it
    character by character with a delay of 1 second"""
    for i in word:
        time.sleep(1)
        print(i, end="")


animation("Hello World")

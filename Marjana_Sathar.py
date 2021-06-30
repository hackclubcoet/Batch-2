#MARJANA SATHAR-2-COUNTDOWN(TIME MODULE)
import time
'''we import time module so we can use sleep which delays time'''
def num():
    '''returns value from 1 to 10 in descending order with a time delay of 1 sec'''
    for i in range(10,0,-1):
        print(i)
        time.sleep(1)
num()

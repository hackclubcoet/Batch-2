# Arjun Ravindran,Batch 2,Body Mass Index
height = float(input("Enter the height in m : ")) # Enter the height 
weight = int(input("Enter the weight in Kg : "))  # Enter the weight
a = weight/(height**2) # bmi formula
bmi = round(a)
if bmi<=18.5: # if bmi is less than 18.5 and then print
     print("Underweight")
elif 18.5 < bmi <=25: # if bmi is between 18.5 and 25 and then print
    print("Normal Weight")
elif 25 < bmi <=30: # if bmi is between 25 and 30 and then print
    print("Slightly Overweight")
elif 30 < bmi <=35 # if  bmi is between 30 and 35
    print("Obese")
else: # if the above statements is wrong and then print
    print("Clinically Obses")

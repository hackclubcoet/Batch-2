height = float(input("Enter the height in m : "))
weight = int(input("Enter the weight in Kg : "))
a = weight/(height**2)
bmi = round(a)
if bmi<=18.5:
     print("Underweight")
elif 18.5 < bmi <=25:
    print("Normal Weight")
elif 25 < bmi <=30:
    print("Slightly Overweight")
elif 30 < bmi <=35:
    print("Obese")
else:
    print("Clinically Obses")
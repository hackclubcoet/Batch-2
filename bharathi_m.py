# BHARATHI_M-BATCH 2-CURRENCY CONVERTER
#CURRENCY CONVERTOR
#CONVERTING USD TO INR OR VICEVERSA ACCORDING TO USERS WISH
user_input = ''


def converter():# TAKES A AMOUNT AND CONVERTS IT FROM INR TO DOLLAR AND VICEVERSA
    print("which currency did you want to convert")
    print("Press a to convert INR to USD")
    print("Press b to convert USD to INR")
    print("Press c to exit ")


while user_input != 'c':
    converter()
    user_input = input("Choose something to continue: ")

    if user_input == 'a': # TO CONVERT INR TO USD
        inr = float(input("Enter the INR Amount you want convert to USD "))
        re = inr * 0.013
        print("The converted currency in USD to INR is ", round(re, 2)) # OUTPUT AMOUNT TO USER

    elif user_input == 'b': # TO CONVERT USD TO INR
        USD = float(input("Enter the USD Amount you want convert to INR  "))
        res = USD * 74
        print("The converted currency in USD to INR is ", round(res, 2)) # OUTPUT AMOUNT TO USER
    elif user_input == 'c':
        print("Bye...")
    else: # IF USER ENTERED SOMETHING ELSE
        print("invalid operation...")
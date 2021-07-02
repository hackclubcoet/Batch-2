# Dictionary containing the list of items
items = {
    1: "Sugar",
    2: "Tomato",
    3: "Chips",
    4: "Biscuits",
    5: "Chocolate",
}

# Dictionary containing the list of price
price = {
    "Sugar": 20,
    "Tomato": 25,
    "Chips": 10,
    "Biscuits": 15,
    "Chocolates": 5,
}

# Initializing total are zero
total = 0

# To print the available items
print("The items available are: ")
print(items)

# To add multiple items to the shopping list
while True:
    # To get the item number from the user
    print("Enter the number for price: ")
    n = int(input())

    # To get the name of the items to search for the price
    name = items[n]
    print("Price :", price[name])

    # To get the quantity of the item and calculate the price
    print("Enter quantity: ")
    q = int(input())
    amount = q * price[name]
    print("Amount = ", amount)

    # To add the amount to the total
    total += amount

    # To check if the customer wants to continue or check out
    flag = 0
    while True:
        print("Enter 1 to continue or 0 to checkout: ")
        choice = int(input())
        if choice == 0:
            flag = 1
            break
        elif choice == 1:
            break
        else:
            print("Invalid input")
    if flag == 1:
        break

# To print the total amount
print("Total amount = ", total, "Rs")

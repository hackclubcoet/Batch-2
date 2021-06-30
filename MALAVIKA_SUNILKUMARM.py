#MALAVIKA SUNIL KUMAR M-2-SHOPPINGCART
def cart():
    '''Display the products'''
    list1 = ['bag','dress','chocolate','biscuit','sanitizer']
    print("menu : ",*list1,sep="\n ")
#list_in_cart = []
#choice = 1
def shoppingcart():
    '''Appending the users choice to the shopping cart'''
    list_in_cart = []
    choice = 1
    while choice == 1:
        cart()
        p = input("name the product that should be entered into the cart:")
        list_in_cart.append(p)
        print("shopping cart:",*list_in_cart,sep="\n")
        # prompts the user for enter number 1 to continue purchasing and stores it in the variable 'choice'.
        choice =int(input("if u want to continue  purchasing,enter 1="))
shoppingcart()

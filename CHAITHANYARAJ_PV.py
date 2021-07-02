#Chaithanyaraj_p_v-Batch2-to_do_project
#simple python to-do project 
#show the additional item to the todo list and ask the user to adding each task at a time of final list

user_input='random'
#create a list for storing items 
data =list()
#we are going to create 3 option  
# 1.Add an item 
#2.view items 
#3.exit   

#let's create a to-do list item using function

def my_list(): 
    print(" MY TO-DO LIST:") 
    print("1. Add an item:")
    print("2. View items:") 
    print("3. Exit:") 

while user_input != '3': 
    my_list() 
    # get user input
    user_input = input("what you want to do?:") 

    if user_input == '1' : 
        item = input("please enter your new todo:") 
        data.append(item)
        #append the item to our list
        print("Your current todo is :"+str(item))   
    #now let's code the '2' part
       
    elif user_input == '2' : 
        print("List of todo items:") 
        for items in data: 
            print(items) 
    #now let's ode the'3' part
    elif user_input == '3' :
        print("good bye")
    else:
        print("please enter a vaild value") 
# so finally its completed let's check it
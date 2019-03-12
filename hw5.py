#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   RCresswell
# Date:  March 10, 2019
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   RCresswell, 3/10/2019, Added code to complete assignment 5
#https://www.tutorialspoint.com/python/python_dictionary.htm

#-- Data --#
# declare variables and constants

objFileName = "Todo.txt"
strData = ""
dicRow = {}
dicRow2 = {}
dicRow3 = {}
lstTable = []

# Step 1 - Load data from a file

print("Items currently to do are: ")
with open('todo.txt') as list:
    todo_items = list.readlines()
print(todo_items)
for item in todo_items:
    task = item.split(",")[0]
    pri = item.split(",")[1]
    dicRow = {task: pri}
    dicRow2[task] = pri

# Step 2 - Display a menu of choices to the user
while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()#adding a new line

    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        print(dicRow2)
        continue
    # Step 4 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        lstTable_u = input("Add a new to do item to the list. ")
        lstTable_p = input("Add a priority to the task: low, high or medium. ")
        dicRow2[lstTable_u] = lstTable_p
        print(dicRow2)
        continue
    # Step 5 - Remove a new item to the list/Table
    elif(strChoice == '3'):
        print(dicRow2)
        lstTable_u = str(input("Which item do you want to remove? "))
        if lstTable_u in dicRow2:
            dicRow2.pop(lstTable_u)
        else:
            print(lstTable_u, "Is not in the list")
            print("These are the items in the list. ", dicRow2)
        continue
    # Step 6 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        objFileName = open('Todo.txt', 'w')
        objFileName.write(str(dicRow2))
        objFileName.close()
    # Step 7 - Exits the program
    elif (strChoice == '5'):
        objFileName = open('Todo.txt', 'w')
        objFileName.write(str(dicRow2))
        objFileName.close()
        break

input("\n\nPress the enter key to exit.")
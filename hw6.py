'''
# Title: Homework 5
# Dev:   RCresswell
# Date:  March 16, 2019
# ChangeLog: (Who, When, What)
1. Re-use the code from your previous assignment
2. Place your code into functions
3. Test your script
4. Upload your python script to canvas
'''

#-- Data --#
task_dict = {}
infile = "ToDo.txt"

# function lets you input file using its name. Loads from relative path.
def loadfile(input):
    with open(input, 'r') as todo_file:
        lines = todo_file.readlines()
        #print(lines)
        #return (lines)
    for line in lines:
        task = line.split(",")[0].strip()
        priority = line.split(",")[1].strip()
        task_dict[task] = priority
    return(task_dict)

#Prints function and dictionary as a test and lets user see whats in the file to start off with
print(loadfile("ToDo.txt"))

#Function to view current dictionary
def view_dic():
    print(task_dict)

#Function to save the file
def save_file():
    with open(infile, 'w') as fh:
        for key, value in task_dict.items():
            fh.write('{},{}\n'.format(key, value))

#Funtion to add items to dictionary
def add_items():
    t = input("Add a new to do item to the list. ")
    p = input("Add a priority to the task: low, high or medium. ")
    task_dict[t] = p
    return(task_dict)

#Function to remove items from dictionary
def remove_items():
    t = str(input("Which item do you want to remove? "))
    if t in task_dict:
        del task_dict[t]
    else:
        print(t, "Is not in the list")
        print("These are the items in the list. ", task_dict)

#Displays a menu of choices to the user
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
    print()
    #Shows the current items in the dictionary
    if (strChoice.strip() == '1'):
        view_dic()
    #Takes input to add items to dictionary
    elif(strChoice.strip() == '2'):
        add_items()
    #Takes input to remove items from dictionary
    elif(strChoice == '3'):
        remove_items()
    #Saves file to the input file variable
    elif(strChoice == '4'):
        save_file()
    #Exits and saves the dictionary file
    elif (strChoice == '5'):
        save_file()
        break

input("\n\nPress the enter key to exit.")
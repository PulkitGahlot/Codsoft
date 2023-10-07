List=[]

def displayList():
    if len(List)==0:
        print("Your List is empty. Add some tasks")
    else :
        for i in List:
            print(i)
    print()

def addToList(task):
    List.append(task)
    print("Task is added")
    print()
    

def delATask(index):
    if len(List)<index-1:
        print(f"There are only {len(List)} tasks. Enter a valid number")
    else:
        del List[index-1]
    print("Task deleted")
    print()

def changeTask(index,changes):
    if len(List)<index-1:
        print(f"There are only {len(List)} tasks. Enter a valid number")
    else:
        List[index-1]=changes
    print("Task is updated")
    


while True:
    userChoice=int(input("Hello There!\nWhat do you want to do:\n1> Add a Task\n2> Delete a Task\n3> Delete the whole List\n4> Show all Tasks\n5> Change a Task\n6> Exit\n"))

    if userChoice==1:
        userInput=input("Type your Task:")
        addToList(userInput)

    elif userChoice==2:
        displayList()
        userInput=int(input("Which Number of Task in List you want to delete:"))
        delATask(userInput)

    elif userChoice==3:
        confirmation=input("Are you sure you want to delete the whole List? [y/n]")
        if confirmation=='y':
            List.clear()
            print("List has been deleted")
        print()

    elif userChoice==4:
        print("Your List of tasks is")
        displayList()

    elif userChoice==5:
        changeChoice=int(input("Which Task you want to change:"))
        change=input("Update your task:")
        changeTask(changeChoice,change)   

    elif userChoice==6:
        break

    else:
        print("Enter a valid action")
        print()
        continue

print("Time to complete the tasks")
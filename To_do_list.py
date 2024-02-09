#A simple To do app in python

#Make an empty dictionary
to_do = {}

#Show tasks
def showTasks():
    with open('todo.txt','r') as file:
        data = file.read()
        print(data)

#Add a new task
def add():
    name = input('Enter your name: ')
    print(f"Hello {name}, Welcome to the to do app")

    # prompt user to input to do
    title = input('Enter title of to do: ')
    title = title.title()
    description = input(f'Enter description of {title}: ')
    new_to_do = {"title":{title},"description":{description}}

    #save the user input
    to_do["task"] = new_to_do

    #Save the input into a new file
    with open('todo.txt','a') as file:
        file.write(f"{title}:{description}")

    showTasks()    

    print('Saved successfully!!!')        

#Remove tasks
def remove():
    remove = input("Enter the title of the to do: ")
    remove = remove.title()
    if(remove in to_do.keys()):
        to_do.pop[remove]
        showTasks()
    else:
        print(f"{remove} does not exitst")    


def welcome():
    print('What would you like to do?')
    print('1  -Add a task')
    print('2  -Remove a task')
    print('3  -Show tasks')

    choice = int(input('Enter choice: '))

    if(choice == 1):
        return add()
    elif(choice == 2):
        remove()
    elif(choice == 3):
        showTasks()    
    else:
        print('Sorry, Invalid input')

welcome()
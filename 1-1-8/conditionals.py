
status = True
grades = [67, 95, 88, 42, 99, 77]

def menu():
    global choice
    print("Welcome to my grading system.")
    print("Press 1 to view grades")
    print("Press 2 to add grades")
    print("Press 3 to remove grades")
    print("Press 4 to convert to letter grades")
    print("Press 5 to exit the program")
    choice = int(input("Enter your choice: "))

def show_grades():
    for grade in grades:
        print(grade)

def add_grade():
    new_grade = int(input("Enter your new grade: "))
    grades.append(new_grade)
    print("You added the grade " + str(new_grade) + " to your list")

def remove_grade():
    print("The following are your grades.  If you wish to simply delete the last one, enter -1")
    show_grades()
    delete_grade = int(input("Which index would you like to delete?"))
    if delete_grade == -1:
        print("You deleted the grade: " + str(grades.pop()))
    else:
        print("You deleted the grade: " + str(grades.pop(delete_grade)))

def letter_grade():


def end_program():
    print("Thank you for using our program.  Have a great day!")

while(status):
    menu()
    if choice ==1:
        show_grades()
    elif choice ==2:
        add_grade()
    elif choice ==3:
        remove_grade()
    elif choice ==4:
        letter_grade()
    elif choice ==5:
        end_program()
        status = False
    else:
        print("Please read the menu carefully and select a valid option.")

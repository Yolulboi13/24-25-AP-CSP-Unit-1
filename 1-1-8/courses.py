#   a118_grades.py
#   This code is incomplete.
my_courses = ["English", "Math", "CS"]
for course in my_courses:
    print("If you wish to end the program, type 'end'. Otherwise, please type 'go'.")
    choice=input("")
    if choice=="go":
        points=int(input("What is your grade in "+course+"?: "))
        if points>=90:
          print("A")
        elif points>=80:
          print("B")
        elif points>=70:
          print("C")
        elif points>=65:
          print("D")
        elif points<65:
          print("F")
    elif choice=="end":
        break
    else:
        print("Please make a valid choice")

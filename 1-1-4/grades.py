grade=int(input("What was the grade you got on your latest test?: "))
if grade>=90:
    print("You got an A!!!")
elif grade>=80 and grade<90:
    print("You got an B!")
elif grade>=70 and grade<80:
    print("You got an C.")
elif grade>=65 and grade<70:
    print("You got an D...")
else:
    print("You failed. Yikes...")
    print("Maybe try again next year?")
# mah favorite number is eleven, thats why its used
# gio likes 852, thats why its used

total = 0
increment = int(input("How much would you like to count by?: ")
goal = int(input("What number would you like to stop on or right before?: "))

while total<goal:
    total+=11
    if total>852:
        total-=11
        break

print("Your total closest to 852 is "+str(total))

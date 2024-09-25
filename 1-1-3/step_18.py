#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = int(input("Enter number of floors to build: "))
color = "gray"

# iterate

for floor in range(num_floors):
        # set placement and color of turtle
    if floor%21==0:
        x+=100
        y=-150
        painter.penup()
        painter.goto(x,y)
        painter.pendown()
    else:
        painter.penup()
        painter.goto(x, y)
        if floor % 3 == 0:
            if color == "gray":
                color = "blue"
            else:
                color = "gray"

        painter.color(color)
        y = y + 5  # location of next floor

        # draw the floor
        painter.pendown()
        painter.forward(50)

wn = trtl.Screen()
wn.mainloop()

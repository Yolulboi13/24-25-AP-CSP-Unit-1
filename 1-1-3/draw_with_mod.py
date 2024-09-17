#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(1)

# starting location of the tower
x = -200
y = -210

# height of tower and a counter for each floor
num_floors = 500
color=painter.color()
color="gray"
# iterate
for floor in range(num_floors):
    # set placement and color of turtle
    painter.penup()
    painter.goto(x, y)
    if floor % 3 == 0:
        if color=="gray":
            color="blue"
        else:
            color="gray"
    y = y + 1  # location of next floor

    # draw the floor
    painter.pendown()
    painter.forward(1000)

wn = trtl.Screen()
wn.mainloop()
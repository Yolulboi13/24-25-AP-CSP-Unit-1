import turtle as trtl
from xml.sax.handler import property_encoding

gojo = trtl.Turtle()
gojo.speed("fastest")

# Makes Gojo's perfect jawline (sigma)
gojo.penup()
gojo.goto(-250,75)
gojo.right(90)
gojo.left(15)
gojo.pendown()
gojo.forward(150)
gojo.left(25)
gojo.forward(100)
gojo.left(50)
gojo.forward(75)
gojo.left(50)
gojo.forward(100)
gojo.left(25)
gojo.forward(150)
gojo.penup()

#Mouth
gojo.goto(-165,-75)
gojo.right(78)
gojo.pendown()

for step in range(2):
    gojo.forward(25)
    gojo.left(5)
    gojo.forward(25)
    gojo.right(5)

gojo.penup()
gojo.left(180)
gojo.forward(15)
gojo.left(80)
gojo.forward(2)
gojo.pendown()
gojo.right(40)
gojo.forward(20)
gojo.right(20)
gojo.forward(20)
gojo.right(30)
gojo.forward(20)
gojo.right(30)
gojo.forward(20)

# Our Glorious King's Nostrils
gojo.penup()
gojo.goto(-115,-50)
gojo.pendown()
gojo.left(180)
for step in range(3):
    gojo.forward(6)
    gojo.left(25)

gojo.penup()
gojo.goto(-125, -50)
gojo.pendown()
gojo.left(180)
for step in range(3):
    gojo.forward(6)
    gojo.right(25)

# My Boy's Boistrously Booming Beautiful Baby Blues (right eye)
gojo.penup()
gojo.goto(-75,25)
gojo.right(70)
gojo.pendown()
gojo.forward(20)
gojo.right(65)
gojo.forward(50)
gojo.right(90)
gojo.forward(20)
gojo.penup()
gojo.goto(-78,25)
gojo.left(155)
gojo.pendown()
gojo.forward(23)
gojo.right(65)
gojo.forward(50)

# My Boy's Boistrously Booming Beautiful Baby Blues (left eye)
gojo.penup()
gojo.goto(-150,25)
gojo.left(110)
gojo.pendown()
gojo.forward(20)
gojo.left(65)
gojo.forward(50)
gojo.left(90)
gojo.forward(20)
gojo.penup()
gojo.goto(-147,25)
gojo.right(155)
gojo.pendown()
gojo.forward(23)
gojo.left(65)
gojo.forward(50)


# The mess of hair
gojo.penup()
gojo.goto(-10,80)



# Turtle go far,,,,,,,,, far away where "unable" to be seen again
gojo.penup()
gojo.goto(99999999,99999999)

wn = trtl.Screen()
wn.mainloop()
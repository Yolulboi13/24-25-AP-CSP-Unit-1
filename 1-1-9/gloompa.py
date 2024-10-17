import turtle as trtl

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
gojo.forward(25)
gojo.left(10)

wn = trtl.Screen()
wn.mainloop()
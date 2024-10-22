import turtle as trtl

from unicodedata import category

cat = trtl.Turtle()
cat.speed(0)

while True:

    #body
    cat.penup()
    cat.goto(0,0)
    cat.pendown()
    cat.circle(100)

    #eyes
    cat.penup()
    cat.goto(0,100)
    cat.pendown()
    cat.fillcolor('black')
    cat.begin_fill()
    cat.circle(10)
    cat.end_fill()
    cat.penup()
    cat.goto(-50,100)
    cat.begin_fill()
    cat.circle(10)
    cat.end_fill()

    #nose and mouth
    cat.penup()
    cat.goto(-30,80)
    cat.begin_fill()
    cat.circle(10,360,3)
    cat.end_fill()
    cat.pendown()
    cat.color("black")
    cat.right(90)
    cat.circle(25,180)
    cat.penup()
    cat.goto(-30,80)
    cat.pendown()
    cat.circle(20,-180)

    #ears
    cat.penup()
    cat.goto(0,0)
    cat.pendown()
    cat.left(90)
    cat.circle(100,120)
    cat.right(30)
    cat.forward(50)
    cat.left(90)
    cat.forward(50)
    #ear 2
    cat.penup()
    cat.goto(0, 0)
    cat.pendown()
    cat.right(180)
    cat.circle(100, 240)
    cat.right(150)
    cat.forward(50)
    cat.right(90)
    cat.forward(50)

    cat.penup()
    cat.right(45)
    cat.goto(-999,-999)
    cat.fillcolor('white')
    cat.begin_fill()
    cat.pendown()
    cat.circle(999,360,4)
    cat.end_fill()

 #body
    cat.left(90)
    cat.penup()
    cat.goto(0,25)
    cat.pendown()
    cat.circle(100)

    #eyes
    cat.penup()
    cat.goto(0,125)
    cat.pendown()
    cat.fillcolor('black')
    cat.begin_fill()
    cat.circle(10)
    cat.end_fill()
    cat.penup()
    cat.goto(-50,125)
    cat.begin_fill()
    cat.circle(10)
    cat.end_fill()

    #nose and mouth
    cat.penup()
    cat.goto(-30,115)
    cat.begin_fill()
    cat.circle(10,360,3)
    cat.end_fill()
    cat.pendown()
    cat.color("black")
    cat.right(90)
    cat.circle(25,180)
    cat.penup()
    cat.goto(-30,115)
    cat.pendown()
    cat.circle(20,-180)

    #ears
    cat.penup()
    cat.goto(0,25)
    cat.pendown()
    cat.left(90)
    cat.circle(100,120)
    cat.right(30)
    cat.forward(50)
    cat.left(90)
    cat.forward(50)
    #ear 2
    cat.penup()
    cat.goto(0, 25)
    cat.pendown()
    cat.right(180)
    cat.circle(100, 240)
    cat.right(150)
    cat.forward(50)
    cat.right(90)
    cat.forward(50)


wn = trtl.Screen()
wn.mainloop()



# hi marcus :D
# herro? yo fone linging
# ur fridge running. then u better keep it pluged in
# pluh
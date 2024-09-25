import turtle as trtl
a=trtl.Turtle()
color=input("Choose a color: ")
a.color(color)
a.speed(0)
step=1
a.goto(0,0)
while True:
    a.forward(step)
    a.right(179)
    a.circle(step,360,50)
    step+=0.5

wn=trtl.Screen()
wn.mainloop()
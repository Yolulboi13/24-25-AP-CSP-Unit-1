import turtle as trtl
a=trtl.Turtle()
color=input("Choose a color: ")
color2=input("Choose another color: ")
current_color=color
a.speed(0)
step=1
a.goto(0,0)
while True:
    a.color("magenta")
    a.forward(step)
    a.right(179)
    a.color(current_color)
    a.circle(step,360,20)
    step+=0.5
    #if step % 2 == 0:
    if current_color==color:
        current_color=color2
    else:
        current_color=color
wn=trtl.Screen()
wn.mainloop()
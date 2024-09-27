import turtle as trtl
a=trtl.Turtle()
step=1
while True:
    a.forward(step/2)
    a.right(step)
    a.circle(step,step,step)
    step+=10

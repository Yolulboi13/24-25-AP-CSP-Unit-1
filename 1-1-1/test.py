import turtle as trtl
guy=trtl.Turtle()
step = 1
guy.speed(10000)
while step<500:
    guy.forward(step)
    step+=1
    guy.right(step/100)
    guy.backward(step)
guy.goto(0,0)
step=1
while True:
    guy.backward(1)
    guy.left(step)
    guy.circle(step,360,step)
    step+=1

wn = trtl.Screen()
wn.mainloop()

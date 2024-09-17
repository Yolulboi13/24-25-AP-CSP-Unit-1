import turtle as trtl
guy=trtl.Turtle()
step = 1
guy.speed(10000)
while step <500:
    guy.forward(step)
    step+=0.1
    guy.right(step/100)
    guy.backward(step)
while True:
    guy.backward(1)
    guy.left(step)
    guy.circle(step,360,step)
    step+=0.1
wn=trtl.Screen()
wn.mainloop()

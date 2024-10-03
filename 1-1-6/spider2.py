import turtle as trtl

painter = trtl.Turtle()
painter.pensize(100)

painter.circle(50,360)
# draw curved arc
painter.pensize(5)
for step in range(8):
  painter.penup()
  painter.goto(0, 25)
  painter.pendown()
  painter.circle(100, 180)
  painter.right(50)

painter.penup()
painter.goto(150,0)
painter.pendown()
painter.circle(10,360)
painter.goto(0,25)
# draw segmented arc
'''
painter.penup()
painter.goto(0, 20)
painter.pendown()
painter.circle(100, 180, 3)
'''
wn = trtl.Screen()
wn.mainloop()
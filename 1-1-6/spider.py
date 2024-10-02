import turtle as trtl

# Sets up the turtle that draws the spider
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
spider.speed(0)

# Sets up how the legs will be drawn
legs = 8
leg_length = 100
rotation = 380 / legs

spider.pensize(5)

# Step is simply just each iteration to make sure the loop doesn't keep going
step = 0

# This part draws the legs
while (step < legs):
  spider.goto(0, 0)
  spider.setheading(rotation * step)
  spider.forward(leg_length)
  step = step + 1

# This part makes sure the turtle isn't visible after it's done drawing the spider
spider.hideturtle()

wn = trtl.Screen()
wn.mainloop()
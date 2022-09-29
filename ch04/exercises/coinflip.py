import turtle
import random

window = turtle.Screen()
window.screensize(800,800)

myturtle = turtle.Turtle()
myturtle.shape("turtle")
myturtle.color("green")

x = turtle.xcor()
y = turtle.ycor()
coords = ([x,y])
i = ([500,500])
while coords <= i:
      coinflip = range(1,3)
      coinflip = random.choice(coinflip)
      if coinflip == 1:
        myturtle.left(90)
      if coinflip == 2:
        myturtle.right(90)
      myturtle.forward(50)
      if coords >= i:
        turtle.bye()


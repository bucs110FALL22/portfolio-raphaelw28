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
      coords = list(myturtle.pos()) #myturtle.pos() returns a tuple. list(myturtle.pos()) puts that tuple into a list. this is necessary since i is a list containing a single tuple, and the comparison on line 25 would throw an error, otherwise.
      print(coords) #prints coords to the console.
      coinflip = range(1,3)
      coinflip = random.choice(coinflip)
      if coinflip == 1:
        myturtle.left(90)
      if coinflip == 2:
        myturtle.right(90)
      myturtle.forward(50)
      if coords >= i: #be careful of using comparison operators on lists/tuples
        #turtle.bye()
        pass #pass does nothing

window.exitonclick() 
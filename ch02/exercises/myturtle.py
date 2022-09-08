import turtle

window = turtle.Screen()

myturtle = turtle.Turtle()

myturtle.shape("turtle")
myturtle.color("purple")

length = 50
sides = 4
angle = 90 
for i in [angle]*(sides):
    myturtle.forward(length)
    myturtle.left(i)

myturtle.color("red")
myturtle.penup()
myturtle.forward(100)
myturtle.pendown()

for i in [angle]*(sides):
    myturtle.forward(length)
    myturtle.left(i)

window.exitonclick()
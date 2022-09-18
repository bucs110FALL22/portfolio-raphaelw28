import turtle

window = turtle.Screen()
myturtle = turtle.Turtle()

myturtle.color("green")
myturtle.shape("turtle")


length = 50
sides = input("Number of sides ")
n = int(sides)
total_degree = int(180*(n - 2))
#angle = float(total_degree / n)
angle = 180 - float(total_degree / n)

for i in [angle]*n:
    myturtle.forward(length)
    myturtle.left(i)
  
window.exitonclick()
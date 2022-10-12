import turtle

def drawEQshape():
  side_length = input("Side Length")
  s = int(side_length)
  sides = input("Number of sides ")
  n = int(sides)
  total_degree = int(180*(n - 2))
  angle = 180 - float(total_degree / n)
  for i in [angle]*n:
    myturtle.forward(s)
    myturtle.left(i)

myturtle = turtle.Turtle()
myturtle.color("green")
myturtle.shape("turtle")
window = turtle.Screen()

drawEQshape()

window.exitonclick()
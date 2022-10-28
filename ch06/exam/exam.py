import pygame
import turtle

pygame.init()
display = pygame.display.set_mode((800,600))
display.fill((255,165,0))

font = pygame.font.Font(None, 50)
msg = font.render("It's almost November so....", False, "black")
display.blit(msg, (100,100))
pygame.display.flip()
pygame.time.wait(1000)

display.fill((255,255,255))
msg = font.render("Turkey Time!", False, "orange")
display.blit(msg, (50,50))
pygame.display.flip()
pygame.time.wait(1000)

height = 800
width = 600
screen = turtle.Screen()
screen.screensize(height,width)

#making the turtle
myturtle = turtle.Turtle()
myturtle.color("black")
myturtle.shape("turtle")
myturtle.speed(0)

def fill_in(x = "color"):
  myturtle.fillcolor(x)
  myturtle.begin_fill()
def move_turtle(x):
  myturtle.penup()
  myturtle.goto(x)
  myturtle.pendown()
  return
def feathers(r = 200, angle=90, n=7):
    for i in range(n):
      for i in range(2):
        myturtle.fillcolor("brown")
        myturtle.begin_fill()
        myturtle.circle(r,angle)
        myturtle.left(180-angle)
        myturtle.end_fill()
      myturtle.left(15)
    return  
def circle(x = "color", y = 0):
  fill_in(x)
  myturtle.circle(y)
  myturtle.end_fill()
  
move_turtle((0,-200))
feathers()
myturtle.right(105)

#head and body
move_turtle((0,0))
circle("beige",50)
circle("orange",-100)
  
#eyes
eye_coords = ((-25,50),(25,50))
myturtle.fillcolor("brown")
for i in eye_coords:
  move_turtle(i)
  myturtle.begin_fill()
  myturtle.circle(10)
  myturtle.end_fill()

#beak
beak_coords = ((-20,40))
move_turtle(beak_coords)
fill_in("yellow")
for i in beak_coords*2:
  myturtle.forward(40)
  myturtle.right(120)
myturtle.end_fill()

#hat
hat_coords = ((-50,100))
move_turtle(hat_coords)
fill_in("black")
myturtle.left(120)
for i in range(4):
  if i% 2 == 0:
      myturtle.forward(100)
      myturtle.left(90)
  else:
    myturtle.forward(20)
    myturtle.left(90) 
myturtle.end_fill()
move_turtle((-30,120))
fill_in("black")
for i in range(4):
  myturtle.forward(60) 
  myturtle.left(90) 
myturtle.end_fill()

#legs
leg_coords = ((10,-200),(-10,-200))
for i in leg_coords:
  move_turtle(i)
  fill_in("black")
  myturtle.circle(-10)
  myturtle.end_fill()

screen.exitonclick()
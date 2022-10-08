import pygame
import random
import math

#Part A
pygame.init()
window = pygame.display.set_mode([300, 300])
window.fill("blue")
pygame.draw.circle(window, "pink", (150, 150), (150))
pygame.draw.line(window, "black", (0, 150), (300, 150))
pygame.draw.line(window, "black", (150, 0), (150, 300))
pygame.display.flip()

#Part B
for i in range(10):
    x = random.randrange(0, 301)
    y = random.randrange(0, 301)
    coords = [x, y]
    print(coords)

    for i in [coords]:
        distance_from_center = math.hypot(x - 150, y - 150)
        is_in_circle = distance_from_center <= 300 / 2
        if is_in_circle == True:
            pygame.draw.circle(window, "green", (coords), (5))
        if is_in_circle == False:
            pygame.draw.circle(window, "red", (coords), (5))
        pygame.display.flip()

#Part C
pygame.time.wait(5000)
window = pygame.display.set_mode([300, 300])
window.fill("black")
blue_team = pygame.draw.rect(window, "blue", pygame.Rect(0, 0, 150, 300))
red_team = pygame.draw.rect(window, "red", pygame.Rect(150, 0, 150, 300))
# pygame.draw.rect(window, "red", pygame.Rect(0, 0, 150, 300))
# pygame.draw.rect(window, "blue", pygame.Rect(150, 0, 150, 300))
pygame.display.flip()

blue_score = 0
red_score = 0
player_selected = ""

team_chosen = False
while not team_chosen:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            (xmouse, ymouse) = pygame.mouse.get_pos()
            if red_team.collidepoint(xmouse, ymouse):
                print("You think Red will win?")
                player_selected = "red"
                team_chosen = True
                pygame.display.flip()
            else:
                print("You think Blue will win?")
                player_selected = "blue"
                team_chosen = True
                pygame.display.flip()


window = pygame.display.set_mode([300, 300])
window.fill("blue")
pygame.draw.circle(window, "pink", (150, 150), (150))
pygame.draw.line(window, "black", (0, 150), (300, 150))
pygame.draw.line(window, "black", (150, 0), (150, 300))
pygame.display.flip()


for i in range(10):
    x = random.randrange(0, 301)
    y = random.randrange(0, 301)
    coords = [x, y]
  
    pygame.draw.circle(window, "red", (coords), (5))
    for i in [coords]:
        distance_from_center = math.hypot(x - 150, y - 150)
        is_in_circle = distance_from_center <= 300 / 2

        if is_in_circle == True:
          red_score +=1
        if is_in_circle == False:
            pygame.draw.circle(window, "yellow", (coords), (5))

    x = random.randrange(0, 301)
    y = random.randrange(0, 301)
    coords = [x, y]

    pygame.draw.circle(window, "blue", (coords), (5))
    for i in [coords]:
        distance_from_center = math.hypot(x - 150, y - 150)
        is_in_circle = distance_from_center <= 300 / 2

        if is_in_circle == True:
          blue_score +=1
        if is_in_circle == False:
            pygame.draw.circle(window, "yellow", (coords), (5))

    pygame.display.flip()
   
print("Blue had", blue_score)
print("Red had", red_score)

if player_selected == "red" and red_score > blue_score:
  print("Player Red Wins!")
  print("You Win!")
if player_selected == "red" and red_score < blue_score:
  print("Player Blue Wins!")
  print("You Lose!")
if player_selected == "blue" and blue_score > red_score:
  print("Player Blue Wins!")
  print("You Win!")
if player_selected == "blue" and blue_score < red_score:
  print("Player Red Wins!")
  print("You Lose!")
if player_selected == "blue" and blue_score == red_score:
  print("Tie!")
  print("No Winner")
if player_selected == "red" and red_score == blue_score:
  print("Tie!")
  print("No Winner")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

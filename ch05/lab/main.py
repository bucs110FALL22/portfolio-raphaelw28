import pygame
pygame.init()
display = pygame.display.set_mode((250,250))
scale = 5
def threenp1(n):
    count = 0
    while (n != 1.0):
       count += 1
       if (n % 2 == 0) == True:
        n = int(n / 2)
       elif (n % 2 == 0) == False:
        n = int(3 * n + 1)
    return count
upper_limit = 20
iters = {}
start = 2
max_so_far = 0
for i in range(start, upper_limit):
  count = threenp1(i)
  iters[i] = count
  if max_so_far < count:
    max_so_far = count
    max_val = count
  coordinates = [(x* scale, y * scale) for x, y in iters.items()]
  display.fill((255,255,255))
  pygame.display.flip
  if len(iters) >= 2:
    pygame.draw.lines(display, "black", False, coordinates)
    new_display = pygame.transform.flip(display, False, True)
    display.blit( new_display , (0, 0) )
    font = pygame.font.Font(None, 30)
    msg = font.render(str(max_so_far), False, "black")
    display.blit(msg, (10,10))
    pygame.display.flip()
    pygame.time.wait(2000)
print(iters)

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      running = False
  
  

class Rectangle:
  def __init__(self, xcoord, ycoord, height, width):
    self.x = xcoord
    self.y = ycoord
    self.width = width
    self.height = height
    if xcoord < 0:
      self.x = 0
    if ycoord < 0:
      self.y = 0
    if width < 0:
      self.width = 0
    if height < 0:
      self.height = 0
  def __str__(self):
    return 'xcoord = {}, ycoord = {}, height = {}, width = {}'.format(self.x, self.y, self.height, self.width)

class Rectangle:
  def __init__(self, x, y, height, width):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    if x < 0:
      self.x = 0
    if y < 0:
      self.y = 0
    if width < 0:
      self.width = 0
    if height < 0:
      self.height = 0
  def __str__(self):
    return 'x = {}, y = {}, height = {}, width = {}'.format(self.x, self.y, self.height, self.width)

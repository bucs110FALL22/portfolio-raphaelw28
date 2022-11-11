from Rectangle import Rectangle
class Surface:
  def __init__(self, image, x,y,h,w):
    self.rect = Rectangle(x, y, h, w)
    self.image = image
  def getRect(self):
      return self.rect
  
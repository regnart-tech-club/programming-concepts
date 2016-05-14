import turtle

# TODO: Explain the 'is-a' type relationship of inheritance
#       versus the 'has-a' type relationship of composition.
class RobotTurtle(object):
  def __init__(self, t, name):
    self.__name = name
    self.__turtle = t
    self.__turtle.color(self.color(name))

  def forward(self):
    self.__turtle.forward(64)

  def left(self):
    self.__turtle.left(90)

  def right(self):
    self.__turtle.right(90)

  def laser(self):
    print self.__name + ' is melting an ice wall!'

  def color(self, name):
    name_color_dictionary = {
      'Pi': 'red',
      'Beep': 'blue',
      'Dot': 'purple',
      'Pangle': 'green'
    }

    return name_color_dictionary[name]

pi = RobotTurtle(turtle.Turtle(), 'Pi')
pi.forward()
pi.left()
pi.laser()
pi.forward()

pangle = RobotTurtle(turtle.Turtle(), 'Pangle')
pangle.right()
pangle.forward()

beep = RobotTurtle(turtle.Turtle(), 'Beep')
beep.left()
beep.forward()
beep.forward()

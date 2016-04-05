import turtle

class DoubleTimeTurtle(turtle.Turtle):
	def forward(self, distance):
		turtle.Turtle.forward(self, 2 * distance)
		
	def backward(self, distance):
		turtle.Turtle.backward(self, 2 * distance)
		
class OppositeTurtle(turtle.Turtle):
	def forward(self, distance):
		turtle.Turtle.backward(self, distance)
		
	def backward(self, distance):
		turtle.Turtle.forward(self, distance)

	def left(self, angle):
		turtle.Turtle.right(self, angle)

	def right(self, angle):
		turtle.Turtle.left(self, angle)
		
regular_turtle = turtle.Turtle()
regular_turtle.color('red')
regular_turtle.left(90)
regular_turtle.forward(64)

double_time_turtle = DoubleTimeTurtle()
double_time_turtle.color('green')
double_time_turtle.left(90)
double_time_turtle.forward(64)

opposite_turtle = OppositeTurtle()
opposite_turtle.color('blue')
opposite_turtle.left(90)
opposite_turtle.forward(64)

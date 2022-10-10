import turtle
from turtle import Turtle, Screen

class Hypergraph:
	def __init__(self, width, height, function, step):
		self.function = function
		self.step = step

		self.width = width
		self.height = height

		self.xMax = width/2
		self.xMin = (width/2)*-1
		self.yMax = height/2
		self.yMin = (height/2)*-1

		self.screen = self.screenSetup()
		self.turtle = self.turtleSetup()

	def screenSetup(self):
		screen = Screen()
		screen.setup(self.width, self.height)
		return screen

	def turtleSetup(self):
		tu = Turtle()
		tu.hideturtle()
		tu.speed(0)
		return tu

	def move(self, x, y):
		self.turtle.penup()
		self.turtle.goto(x, y)
		self.turtle.pendown()

	def originMark(self):
		self.move(-10, -15)
		self.turtle.write("O")

	def drawX(self):
		self.move(self.xMax, 0)
		self.turtle.goto(self.xMin, 0)

	def drawY(self):
		self.move(0, self.yMax)
		self.turtle.goto(0, self.yMin)

	def contourX(self, grad):
		self.move(0, 0)

		goX = 0
		while (self.xMin < goX):
			goX += (grad)*-1
			self.move(goX, 5)
			self.turtle.goto(goX, -5)

			self.move(goX-5, -20)
			self.turtle.write(goX)

		backX = 0
		while (self.xMax > backX):
			backX += grad
			self.move(backX, 5)
			self.turtle.goto(backX, -5)

			self.move(backX-8, -20)
			self.turtle.write(backX)

	def contourY(self, grad):
		self.move(0, 0)

		goY = 0
		while (self.yMin < goY):
			goY += (grad)*-1
			self.move(5, goY)
			self.turtle.goto(-5, goY)

			self.move(10, goY-8)
			self.turtle.write(goY)

		backY = 0
		while (self.yMax > backY):
			backY += grad
			self.move(5, backY)
			self.turtle.goto(-5, backY)

			self.move(10, backY-8)
			self.turtle.write(backY)

	@staticmethod
	def BetterRange(start, stop, step=1):
		rangeList = []
		rangeList = [*rangeList, *reversed(range(0, start, step))]
		rangeList = [*rangeList, *[i*-1 for i in list(range(0, stop*-1, step))]]
		return list(reversed(sorted(list(set(rangeList)))))

	def drawFunc(self):
		xList = Hypergraph.BetterRange(int(self.xMax), int(self.xMin), self.step)
		self.move(self.xMax, self.function(int(self.xMax)))
		for x in xList:
			y = self.function(x)
			self.turtle.goto(x, y)

if __name__ == '__main__':
	func = lambda x: -1*(((1/10)*x)**2)
	hg = Hypergraph(512, 512, func, 10)
	hg.originMark()
	hg.drawX()
	hg.drawY()
	hg.contourX(30)
	hg.contourY(30)
	hg.drawFunc()

	turtle.exitonclick()
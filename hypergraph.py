import re
import turtle
import decimal

from turtle import Turtle, Screen
from tkinter import TclError


class Hypergraph:
    def __init__(self, width, height, function, ratio=1, step=3):
        self.function = function
        self.step = step
        self.ratio = ratio

        self.width = width
        self.height = height

        self.xMax = width/2
        self.xMin = (width/2)*-1
        self.yMax = height/2
        self.yMin = (height/2)*-1

        self.xList = Hypergraph._BetterRange(
            int(self.xMax), int(self.xMin), self.step
        )

        self.screen = self._screenSetup()
        self.turtle = self._turtleSetup()

    def _screenSetup(self):
        screen = Screen()
        screen.setup(self.width, self.height)
        return screen

    def _turtleSetup(self):
        tu = Turtle()
        tu.hideturtle()
        tu.speed(0)
        return tu

    def _move(self, x, y):
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()

    def originMark(self):
        self._move(-10, -15)
        self.turtle.write("O")

    def drawX(self):
        self._move(self.xMax, 0)
        self.turtle.goto(self.xMin, 0)

    def drawY(self):
        self._move(0, self.yMax)
        self.turtle.goto(0, self.yMin)

    def contourX(self, grad):
        if grad <= 0:
            return None

        self._move(0, 0)

        goX = 0
        while (self.xMin < goX):
            goX += (grad)*-1
            self._move(goX, 5)
            self.turtle.goto(goX, -5)

            self._move(goX-5, -20)
            self.turtle.write(goX)

        backX = 0
        while (self.xMax > backX):
            backX += grad
            self._move(backX, 5)
            self.turtle.goto(backX, -5)

            self._move(backX-8, -20)
            self.turtle.write(backX)

    def contourY(self, grad):
        if grad <= 0:
            return None
        self._move(0, 0)

        goY = 0
        while (self.yMin < goY):
            goY += (grad)*-1
            self._move(5, goY)
            self.turtle.goto(-5, goY)

            self._move(10, goY-8)
            self.turtle.write(goY)

        backY = 0
        while (self.yMax > backY):
            backY += grad
            self._move(5, backY)
            self.turtle.goto(-5, backY)

            self._move(10, backY-8)
            self.turtle.write(backY)

    @staticmethod
    def _BetterRange(start, stop, step=1):
        rangeList = []
        rangeList = [*rangeList, *reversed(range(0, start, step))]
        rangeList = [*rangeList, *
                     [i*-1 for i in list(range(0, stop*-1, step))]]
        return list(reversed(sorted(list(set(rangeList)))))

    @staticmethod
    def Parse(string: str):
        string = string.lower()
        string = string.replace("^", "**")
        roots = re.findall(r"root\((.+?)\)", string)
        for rt in roots:
            string = string.replace(f'root({rt})', f"(({rt})**(1/2))")
        return string

    def _drawFunc(self, track=lambda x: x):
        self._move(self.xMax, self.function(int(self.xMax)))
        for x in track(self.xList):
            try:
                y = self.function(x)
            except ZeroDivisionError as e:
                if y > 0:
                    self.turtle.goto(x, self.yMax)
                else:
                    self.turtle.goto(x, self.yMin)

                x = self.xList[self.xList.index(x) + 1]
                y = self.function(x)
                self._move(x, y)

                if y > 0:
                    self.turtle.goto(x, self.yMax)
                else:
                    self.turtle.goto(x, self.yMin)
            else:
                try:
                    if type(y) != complex:
                        if y > 0:
                            if y <= (self.yMax + (self.yMax/2)):
                                self.turtle.goto(x, y)
                        else:
                            if y >= (self.yMin + (self.yMin/2)):
                                self.turtle.goto(x, y)
                except TclError:
                    pass
            yield x, y

    def Graph(self):
        for x, y in self._drawFunc():
            pass
        self._move(0, 0)


if __name__ == '__main__':
    def func(x): return -1*(((1/10)*x)**2)
    hg = Hypergraph(512, 512, func, 10)
    hg.originMark()
    hg.drawX()
    hg.drawY()
    hg.contourX(30)
    hg.contourY(30)
    hg.Graph()

    turtle.exitonclick()

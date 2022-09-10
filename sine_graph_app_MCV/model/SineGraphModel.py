import math
import numpy

class SineGraphModel:

    def __init__(self, controller, xVals: list[float] = numpy.arange(-2, 2, 0.0001), a: int = 1, f: int = 1) -> None:
        self.controller = controller
        self.xVals = xVals
        self.a = a
        self.f = f
        self.yVals = self.getYVals()

    def getYVals(self):
        self.yVals = [self.a*math.sin(2*math.pi*self.f*t) for t in self.xVals]
        return self.yVals

    def getXVals(self):
        return self.xVals

    def getA(self):
        return self.a

    def getF(self):
        return self.f

    def getStrA(self):
        return str(self.a)

    def getStrF(self):
        return str(self.f)

    def updateAandFandYVals(self, new_a, new_f):
        self.a = new_a
        self.f = new_f
        self.getYVals()
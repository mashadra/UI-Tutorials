import math
import numpy

class SineGraphModel:

    def __init__(self, controller, xVals: list[float] = numpy.arange(-2, 2, 0.0001), a: int = 1, f: int = 1) -> None:
        """Initializes a model of a sine graph

        Args:
            controller (SineGraphController): the controller that connectes this model to a view
            xVals (list[float], optional): The x range for the sine graph. Defaults to numpy.arange(-2, 2, 0.0001).
            a (int, optional): The amplitude of the sine graph. Defaults to 1.
            f (int, optional): The frequency of the sine graph. Defaults to 1.
        """

        self.controller = controller
        self.xVals = xVals
        self.a = a
        self.f = f
        self.getYVals()

    def getYVals(self) -> list[float]:
        """Calculates the y values with the x values, amplitude, and frequency set

        Returns:
            list[float]: the y values
        """

        self.yVals = [self.a*math.sin(2*math.pi*self.f*t) for t in self.xVals]
        return self.yVals

    def getXVals(self) -> list[float]:
        """Getter for the x values

        Returns:
            list[float]: the x values
        """

        return self.xVals

    def getA(self) -> int:
        """Getter for the amplitude

        Returns:
            int: the amplitude
        """

        return self.a

    def getF(self) -> int:
        """Getter for the frequency

        Returns:
            int: the frequency
        """

        return self.f

    def getStrA(self) -> str:
        """Returns the amplitude as a string

        Returns:
            str: the amplitude represented as a string
        """

        return str(self.a)

    def getStrF(self) -> str:
        """Returns the frequency as a string

        Returns:
            str: the frequency represented as a string
        """

        return str(self.f)

    def updateAandFandYVals(self):
        """Updates all of the parameters to match what are the values for the amplitude and frequency in the view
        """

        self.a = self.controller.getViewA()
        self.f = self.controller.getViewF()
        self.getYVals()
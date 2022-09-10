import view.SineGraphView as v
import model.SineGraphModel as m

class SineGraphController:

    def __init__(self) -> None:  
        """Initializes a controller
        """

        self.model = m.SineGraphModel(self)
        self.view = v.SineGraphView(self)
        
    def getYVals(self) -> list[float]:
        """Gets the y values from the model

        Returns:
            list[float]: the y values
        """

        return self.model.getYVals()

    def getXVals(self) -> list[float]:
        """Gets the x values from the model

        Returns:
            list[float]: the x values
        """

        return self.model.getXVals()

    def getA(self) -> int:
        """Gets the amplitude from the model

        Returns:
            int: the amplitude
        """

        return self.model.getA()

    def getF(self) -> int:
        """Gets the frequency from the model

        Returns:
            int: the frequency
        """

        return self.model.getF()

    def getStrA(self) -> str:
        """Gets the amplitude from the model as a string

        Returns:
            str: a string representation of the amplitude
        """

        return self.model.getStrA()

    def getStrF(self) -> str:
        """Gets the frequency from the model as a string

        Returns:
            str: a string representation of the frequency
        """

        return self.model.getStrF()

    def updateAandFandYVals(self):
        """Updates all parameters except the x values in the model
        """

        self.model.updateAandFandYVals()

    def getViewA(self) -> int:
        """Gets the value of the amplitude slider in the view

        Returns:
            int: the value of the amplitude slider
        """

        return self.view.getViewA()

    def getViewF(self) -> int:
        """Gets the value of the frequency slider in the view

        Returns:
            int: the value of the frequency slider
        """

        return self.view.getViewF()

    def runApp(self):
        """Runs the app in the view
        """

        self.view.runApp()
import view.SineGraphView as v
import model.SineGraphModel as m

class SineGraphController:

    def __init__(self) -> None:       
        self.model = m.SineGraphModel(self)
        self.view = v.SineGraphView(self)
        
    def getYVals(self):
        return self.model.getYVals()

    def getXVals(self):
        return self.model.getXVals()

    def getA(self):
        return self.model.getA()

    def getF(self):
        return self.model.getF()

    def getStrA(self):
        return self.model.getStrA()

    def getStrF(self):
        return self.model.getStrF()

    def updateAandFandYVals(self):
        self.model.updateAandFandYVals()

    def getViewA(self):
        return self.view.getViewA()

    def getViewF(self):
        return self.view.getViewV()

    def runApp(self):
        self.view.app.exec_()
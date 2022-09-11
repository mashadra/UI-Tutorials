import view.SaveInputView as v
import model.SaveInputModel as m

class SaveInputController:

    def __init__(self) -> None:       
        self.model = m.SaveInputModel(self)
        self.view = v.SaveInputView(self)

    def runApp(self):
        """executes the app in the view
        """

        self.view.runApp()

    def clearTextbox(self):
        """Clears the textbox in the view
        """

        self.view.clearTextbox()

    def getTextboxText(self) -> str:
        """Gets the textbox text frmo the view

        Returns:
            str: the text in the textbox
        """

        return self.view.getTextboxText()

    def saveData(self):
        """Calls the function in the model to save the data in the textbox
        """

        self.model.saveData()
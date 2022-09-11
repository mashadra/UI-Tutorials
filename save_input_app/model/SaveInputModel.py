class SaveInputModel:

    def __init__(self, controller) -> None:  
        """Initializes a mdel for the save_input app

        Args:
            controller (SaveInputController): the controller that connects this model to a view
        """

        self.controller = controller

    def saveData(self):
        """Saves data in the input area to "myFile.txt" and clears the input area
        """

        # saving the data
        with open("myFile.txt", "w") as f:
            f.write(self.controller.getTextboxText())

        # clearing the textbox
        self.controller.clearTextbox()
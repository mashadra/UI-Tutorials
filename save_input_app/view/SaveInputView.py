from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit, QVBoxLayout

class SaveInputView:

    def __init__(self, controller) -> None: 
        """Initializes a view for the save_input app

        Args:
            controller (SaveInputController): The controller that connects this view to a model
        """

        self.controller = controller

        self.app = QApplication([])

        # a text label to instruct a user
        self.instructions = QLabel("Input your data into the textbox then press the 'save' button to save it")

        # a textbox to contain input
        self.textbox = QLineEdit()

        # a button to save input
        self.save_button = QPushButton()
        self.save_button.setText("Save")
        self.save_button.clicked.connect(controller.saveData)

        # laying out the GUI in a box
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.instructions)
        self.layout.addWidget(self.textbox)
        self.layout.addWidget(self.save_button)

        # making a window, adding the layout to it, and displaying it
        self.window = QWidget()
        self.window.setWindowTitle("Save Input")
        self.window.setLayout(self.layout)
        self.window.show()

    def runApp(self):
        """executes the app
        """

        self.app.exec_()

    def clearTextbox(self):
        """Clears the textbox
        """

        self.textbox.setText("")

    def getTextboxText(self) -> str:
        """Gets the text in the textbox

        Returns:
            str: the text in the textbox
        """

        return self.textbox.text()
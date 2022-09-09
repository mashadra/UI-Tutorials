### a script that makes a GUI containing a textbox and a button. When the button is pressed, the contents of the textbox are saved to 'myFile.txt'
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit, QVBoxLayout

### functions

def save_data():
    """Saves data in the input area to "myFile.txt" and clears the input area
    """

    # saving the data
    with open("myFile.txt", "w") as f:
        f.write(textbox.text())

    # clearing the textbox
    textbox.setText("")

### The interface

app = QApplication([])

# a text label to instruct a user
instructions = QLabel("Input your data into the textbox then press the 'save' button to save it")

# a textbox to contain input
textbox = QLineEdit()

# a button to save input
save_button = QPushButton()
save_button.setText("Save")
save_button.clicked.connect(save_data)

# laying out the GUI in a box
layout = QVBoxLayout()
layout.addWidget(instructions)
layout.addWidget(textbox)
layout.addWidget(save_button)

# making a window, adding the layout to it, and displaying it
window = QWidget()
window.setWindowTitle("Save Input")
window.setLayout(layout)
window.show()

# executing everything above
app.exec_()
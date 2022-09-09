from PyQt5.QtWidgets import QApplication, QLabel

# need this for every app I make
app = QApplication([])

# a text label
label = QLabel("Hello World")
label.show()

# executing everything above
app.exec_()
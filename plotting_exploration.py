from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel
import pyqtgraph

app = QApplication([])

# defining a top-level widget to hold everything
w = QWidget()

# making plot
xVals = [0, 1, 2, 3]
yVals = [0, 1, 3, 2]

plot = pyqtgraph.PlotWidget()
plot.plot(xVals, yVals, pen='r')

# making some text
label = QLabel("Graphs are happening")

# setting up layout
layout = QGridLayout()
w.setLayout(layout)

# adding components to layout
layout.addWidget(label)
layout.addWidget(plot)

w.show()

app.exec_()
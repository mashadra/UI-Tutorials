from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout,QWidget
from pyqtgraph import opengl, glColor
import numpy

SIZE = 200

# coordinates to place the point at
x = 50
y = 50
z = 50

# overall app
app = QApplication([])

# defining a top-level widget to hold everything for the graph
w = opengl.GLViewWidget()

# a button to reset rotation and zoom
def reset_view(self):
    global w
    w.setCameraPosition(distance=SIZE*2, elevation=20, azimuth=45)
    w.show()

reset_button = QPushButton()
reset_button.setText("Reset")
reset_button.clicked.connect(reset_view)

# making plot
arr = []
for i in range(0,SIZE):
    arr += [(0, 0, i), (0, i, 0), (i, 0, 0)]
axis_pts = numpy.array(arr)
axis_clrs = glColor("#ffffff")
axis_sze = 0.1

pts = numpy.array([(x, y, z)])
clrs = glColor("#0004ff")
sze = 10

# making one point
graph = opengl.GLScatterPlotItem()
graph.setData(pos=pts, color=clrs, size=sze)

# making points for axis
axis = opengl.GLScatterPlotItem()
axis.setData(pos=axis_pts, color=axis_clrs, size=axis_sze)

# adding components to layout
w.addItem(axis)
w.addItem(graph)
reset_view(w)

# setting up the view
layout = QVBoxLayout()
layout.addWidget(reset_button)

# making a window, adding the layout to it, and displaying it
window = QWidget()
window.setWindowTitle("Plot")
window.setLayout(layout)
window.show()

app.exec_()

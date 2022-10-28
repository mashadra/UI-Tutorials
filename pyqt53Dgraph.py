from PyQt5.QtWidgets import QApplication
from pyqtgraph import opengl, glColor
import numpy

app = QApplication([])

# defining a top-level widget to hold everything
w = opengl.GLViewWidget()

# making plot
arr = []
for i in range(0,200):
    arr += [(0, 0, i), (0, i, 0), (i, 0, 0)]
axis_pts = numpy.array(arr)
axis_clrs = glColor("#ffffff")
axis_sze = 0.1

pts = numpy.array([(50, 50, 50)])
clrs = glColor("#0004ff")
sze = 10

graph = opengl.GLScatterPlotItem()
graph.setData(pos=pts, color=clrs, size=sze)

axis = opengl.GLScatterPlotItem()
axis.setData(pos=axis_pts, color=axis_clrs, size=axis_sze)

# adding components to layout
w.addItem(axis)
w.addItem(graph)
w.setCameraPosition(distance=400)
w.orbit(0, 0)

w.show()

app.exec_()
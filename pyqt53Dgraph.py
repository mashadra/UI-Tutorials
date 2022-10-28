from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout,QWidget
from pyqtgraph import opengl, glColor
import numpy

class plot:

    def __init__(self, size:int=200, x:int=50, y:int=50, z:int=50) -> None:
        self.size = size

        # coordinates to place the point at
        self.x = 50
        self.y = 50
        self.z = 50

        # overall app
        self.app = QApplication([])

        # defining a top-level widget to hold everything for the graph
        self.w = opengl.GLViewWidget()

        self.reset_button = QPushButton()
        self.reset_button.setText("Reset")
        self.reset_button.clicked.connect(self.reset_view)

        # making plot
        arr = []
        for i in range(0,self.size):
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
        self.w.addItem(axis)
        self.w.addItem(graph)
        self.reset_view()

        # setting up the view
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.reset_button)

        # making a window, adding the layout to it, and displaying it
        self.window = QWidget()
        self.window.setWindowTitle("Plot")
        self.window.setLayout(self.layout)
        

    # a button to reset rotation and zoom
    def reset_view(self):
        self.w
        self.w.setCameraPosition(distance=self.size*2, elevation=20, azimuth=45)
        self.w.show()

    def run_app(self):
        self.window.show()
        self.app.exec()

practice = plot()
practice.run_app()

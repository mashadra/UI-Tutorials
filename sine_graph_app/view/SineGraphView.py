from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel,QSlider
from PyQt5.QtCore import Qt
import pyqtgraph

class SineGraphView:

    def __init__(self, controller, min_amp:int = 1, max_amp: int = 10, min_freq: int = 1, max_freq: int = 10) -> None:
        """Initializes all of the elements in the window and lays them out

        Args:
            controller (SineGraphController): The controller that connects this view to a model
            min_amp (int, optional): The minimum ampiltude for the slider. Defaults to 1.
            max_amp (int, optional): The maximum amplitude for the slider. Defaults to 10.
            min_freq (int, optional): The minimum frequency for the slider. Defaults to 1.
            max_freq (int, optional): The maximum frequency for the slider. Defaults to 10.
        """

        self.controller = controller

        # creating GUI components
        self.app = QApplication([])

        # defining a top-level widget to hold everything
        self.w = QWidget()
        self.w.setWindowTitle("Sine Wave")

        # making plot
        self.plot = pyqtgraph.PlotWidget()
        self.plot.plot(self.controller.getXVals(), self.controller.getYVals(), pen='r')

        # making sliders
        self.amp_slider = QSlider()
        self.amp_slider.setMinimum(min_amp)
        self.amp_slider.setMaximum(max_amp)
        self.amp_slider.setTickInterval(1)
        self.amp_slider.valueChanged.connect(self.update_values)

        self.freq_slider = QSlider()
        self.freq_slider.setMinimum(min_freq)
        self.freq_slider.setMaximum(max_freq)
        self.freq_slider.setTickInterval(1)
        self.freq_slider.valueChanged.connect(self.update_values)

        # making some text for instructions and the sliders
        self.label = QLabel("Use the sliders to adjust the amplitude and frequency of the sine wave!")
        self.amp_label = QLabel("Amplitude")
        self.freq_label = QLabel("Frequency")
        self.amp_value = QLabel(self.controller.getStrA())
        self.freq_value = QLabel(self.controller.getStrF())

        # setting up layout
        self.layout = QGridLayout()
        self.w.setLayout(self.layout)

        # adding components to layout
        # parameters go in the order row, column, row span, column span
        self.layout.addWidget(self.label, 0,  0, 1, 2, Qt.AlignCenter)
        self.layout.addWidget(self.plot, 1, 0, 1, 2, Qt.AlignCenter)
        self.layout.addWidget(self.amp_label, 2, 0, 1, 1, Qt.AlignCenter)
        self.layout.addWidget(self.freq_label, 2, 1, 1, 1, Qt.AlignCenter)
        self.layout.addWidget(self.amp_slider, 3, 0, 1, 1, Qt.AlignCenter)
        self.layout.addWidget(self.freq_slider, 3, 1, 1, 1, Qt.AlignCenter)
        self.layout.addWidget(self.amp_value, 4, 0, 1, 1, Qt.AlignCenter)
        self.layout.addWidget(self.freq_value, 4, 1, 1, 1, Qt.AlignCenter)

        self.w.show()

    def update_values(self):
        """Updates all values impacted when a slider is moved
        """

        # creating a new plot
        self.plot.clear()
        self.controller.updateAandFandYVals()
        self.plot.plot(self.controller.getXVals(), self.controller.getYVals(), pen='r')

        # updating the labels by the sliders
        self.amp_value.setText(self.controller.getStrA())
        self.freq_value.setText(self.controller.getStrF())

    def getViewA(self) -> int:
        """Gets the value of the amplitude slider

        Returns:
            int: the value of the amplitude slider
        """

        return self.amp_slider.value()

    def getViewF(self) -> int:
        """Gets the value of the frequency slider

        Returns:
            int: the value of the frequency slider
        """

        return self.freq_slider.value()

    def runApp(self):
        """executes the app
        """

        self.app.exec_()
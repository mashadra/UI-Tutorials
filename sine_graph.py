### making a plot of a sine wave with slider adjustable frequency and amplitude
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel,QSlider
from PyQt5.QtCore import Qt
import pyqtgraph
import math
import numpy

### variables

a = 1
f = 1
xVals = numpy.arange(-2, 2, 0.0001)
yVals = [a*math.sin(2*math.pi*f*t) for t in xVals]

### functions

def change_values():
    """Updates all values impacted when a slider is moved
    """

    # updating the amplitude and frequency globally
    global a
    global f
    a = amp_slider.value()
    f = freq_slider.value()

    # updating the y values to plot
    global yVals
    yVals = [a*math.sin(2*math.pi*f*t) for t in xVals]
    
    # creating a new plot
    plot.clear()
    plot.plot(xVals, yVals, pen='r')

    # updating the labels by the sliders
    amp_value.setText(str(a))
    freq_value.setText(str(f))

### creating GUI components

app = QApplication([])

# defining a top-level widget to hold everything
w = QWidget()
w.setWindowTitle("Sine Wave")

# making plot
plot = pyqtgraph.PlotWidget()
plot.plot(xVals, yVals, pen='r')

# making sliders
amp_slider = QSlider()
amp_slider.setMinimum(1)
amp_slider.setMaximum(10)
amp_slider.setTickInterval(1)
amp_slider.valueChanged.connect(change_values)

freq_slider = QSlider()
freq_slider.setMinimum(1)
freq_slider.setMaximum(10)
freq_slider.setTickInterval(1)
freq_slider.valueChanged.connect(change_values)

# making some text for instructions and the sliders
label = QLabel("Use the sliders to adjust the amplitude and frequency of the sine wave!")
amp_label = QLabel("Amplitude")
freq_label = QLabel("Frequency")
amp_value = QLabel(str(a))
freq_value = QLabel(str(f))

# setting up layout
layout = QGridLayout()
w.setLayout(layout)

# adding components to layout
# parameters go in the order row, column, row span, column span
layout.addWidget(label, 0,  0, 1, 2, Qt.AlignCenter)
layout.addWidget(plot, 1, 0, 1, 2, Qt.AlignCenter)
layout.addWidget(amp_label, 2, 0, 1, 1, Qt.AlignCenter)
layout.addWidget(freq_label, 2, 1, 1, 1, Qt.AlignCenter)
layout.addWidget(amp_slider, 3, 0, 1, 1, Qt.AlignCenter)
layout.addWidget(freq_slider, 3, 1, 1, 1, Qt.AlignCenter)
layout.addWidget(amp_value, 4, 0, 1, 1, Qt.AlignCenter)
layout.addWidget(freq_value, 4, 1, 1, 1, Qt.AlignCenter)

w.show()

app.exec_()
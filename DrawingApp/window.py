import sys
from PyQt5 import *
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton, QSlider
from canvas import Canvas


COLORS = [
    '#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#008080', '#9a6324', '#000075', '#808080', '#000000' 
 ]


class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		# first lets create a widget to serve as our central widget
		# this will be the one that holds our painting
		centralWidget = QWidget()

		# next a layout will help keep things looking nice
		centralLayout = QVBoxLayout()
		centralLayout.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
		centralWidget.setLayout(centralLayout)

		# create a layout for our pen style settings
		self.styleLayout = QHBoxLayout()
		
		# create the slider bar and
		# set the slider bar parameters
		self.slider = QSlider(Qt.Horizontal)
		self.slider.setMinimum(1)
		self.slider.setMaximum(15)
		self.slider.setValue(1)
		self.slider.setTickInterval(1)
		self.slider.setTickPosition(QSlider.TicksBelow)
		self.slider.valueChanged.connect(self.sliderMoved)

		# create a "spray" button 
		self.sprayButton = QPushButton()
		self.sprayButton.setIcon(QIcon("./icons/spray-can.png"))
		self.sprayButton.setIconSize(QSize(25, 25))
		self.sprayButton.setCheckable(True)
		self.sprayButton.clicked.connect(self.toggleSpray)

		# add some labels to the slider bar
		penLabel = QLabel("Pen Size:")
		penLabel.setAlignment(Qt.AlignHCenter)
		self.sliderLabel = QLabel('1')
		self.sliderLabel.setAlignment(Qt.AlignVCenter)
		
		# add the created widgets to the layout
		self.styleLayout.addWidget(penLabel)
		self.styleLayout.addWidget(self.slider, 20)
		self.styleLayout.addWidget(self.sliderLabel, 80)
		self.styleLayout.addWidget(self.sprayButton)

		# add the style layout to the central layout
		centralLayout.addLayout(self.styleLayout)

		# now lets create a painting label to add to our layout
		self.canvas = Canvas()
		# add the canvas to the widget 
		centralLayout.addWidget(self.canvas)

		# lets add the color tray and buttons	
		colorTray = QHBoxLayout()
		self.addColorButtons(colorTray)
		centralLayout.addLayout(colorTray)

		# now lets make this our central widget
		self.setCentralWidget(centralWidget)


	def toggleSpray(self):
		if self.sprayButton.isChecked():
			self.canvas.changePenStyle(1)
		else:
			self.canvas.changePenStyle(0)


	def sliderMoved(self):
		self.canvas.changePenWidth(self.slider.value())
		self.sliderLabel.setText(str(self.slider.value()))


	def addColorButtons(self, layout):
		for c in COLORS:
			button = QPushButton()
			button.setStyleSheet("background-color: %s;" % c)
			button.pressed.connect(lambda color=c: self.canvas.changePenColor(color))
			button.setMaximumWidth(80)
			layout.addWidget(button)



if __name__ == '__main__':
	app = QApplication(sys.argv)

	window = Window()
	window.show()

	app.exec()

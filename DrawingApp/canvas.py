'''
    picture.py
    Dylan Lee
    8/31/20201

    Class to implement a picture canvas for drawing using PyQt
'''

import sys
import random
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter, QPixmap, QPen
from PyQt5.QtWidgets import QLabel


class Canvas(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # first create our pixmap
        pixmap = QPixmap(900,600)
        pixmap.fill(QColor("white"))
        self.setPixmap(pixmap)

        # now we need to set where our previous(initial) mouse pos was
        self.prevX = None
        self.prevY = None

        # set up our QPen, initilize the color and type
        self.pen = QPen()
        self.pen.setCapStyle(Qt.RoundCap)
        self.pen.setColor(QColor('#000000'))
        self.pen.setWidth(1)
        self.spray = 0


    def changePenColor(self, c):
        self.pen.setColor(QColor(c))


    def changePenWidth(self, w):
        self.pen.setWidth(w)

    
    def changePenStyle(self, s):
        self.spray = s
    

    def mouseMoveEvent(self, e):
        if self.prevX is None:
            self.prevX = e.x()
            self.prevY = e.y()
            return
        
        # first we need to create a QPainter instance and pass it our paint area
        painter = QPainter(self.pixmap())
        painter.setPen(self.pen)

        if(self.spray == 1):
            for i in range(50):
                xOffset = random.gauss(0, 20)
                yOffset = random.gauss(0, 20)
                painter.drawPoint(xOffset + e.x(), yOffset + e.y())
        else:
            # now we actually draw a line
            painter.drawLine(self.prevX, self.prevY, e.x(), e.y())
        
        painter.end()        
        self.update()

        # we also need to update the previous position (where we finished)
        self.prevX = e.x()
        self.prevY = e.y()


    def mouseReleaseEvent(self, e):
        self.prevX = None
        self.prevY = None
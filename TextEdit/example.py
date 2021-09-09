'''
File: example.py
Author: Dylan Lee
Date: 8/30/2021
Description:
    simple examples of using PyQt6
'''

import sys
from pathlib import Path
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import *

class OurWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # create a self, mess with the size/position, and add a title
        self.setWindowTitle("Our Example App")
        self.setGeometry(500, 500, 500, 500)

        # create a central widget
        self.central_widget = QWidget()

        # create a layout for the central widget
        #layout = QVBoxLayout()

        # a text box for the central layout
        self.text_box = QTextEdit()

        # add the text box
        #layout.addWidget(self.text_box)

        # set the layout (including the text box) for the central widget
        #self.central_widget.setLayout(layout)

        # set the widget for the central widget of the QMainWindow
        self.setCentralWidget(self.text_box)

        # create a status bar using the built in one for QMainWindow
        self.statusBar().showMessage('Important Status...')

        # create some toolbar buttons using the built in menubar feature of QMainWindow
        self.file_menu = self.menuBar().addMenu("File")
        self.menuBar().addMenu("Edit")

        # add options to the new menu buttons
        # icons make things look nicer
        save_icon = QIcon.fromTheme('document-save')
        self.save_action = QAction(save_icon, 'Save', self)
        self.save_action.setShortcut("Ctrl+S")
        self.save_action.triggered.connect(self.SaveEvent)
        self.file_menu.addAction(self.save_action)


    def SaveEvent(self):
        buffer = self.text_box.toPlainText()
        print(buffer)
        file_dialog = QFileDialog(self)
        
        fileName = file_dialog.getSaveFileName(self, "Save File")
        print(fileName)
        
        f = open(fileName[0], 'w')
        f.write(buffer)
        f.close()
        
        self.statusBar().showMessage('Saved')


if __name__ == '__main__':
    app = QApplication(sys.argv) 
    
    window = OurWindow()
    window.show()
    
    sys.exit(app.exec())
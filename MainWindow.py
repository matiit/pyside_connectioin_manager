import PySide

from PySide.QtGui import *
from PySide.QtCore import Slot


class MainWindow(QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.newButton = QPushButton("Add new connection")
        self.listWidget = QListWidget(self)
        self.listWidget.addItem("Item_1")

        self.grid = QGridLayout()
        self.grid.addWidget(self.newButton, 0, 0)
        self.grid.addWidget(self.listWidget, 1, 0)

        self.setLayout(self.grid)

        self.newButton.clicked.connect(self.clickedNewButton)

    @Slot()
    def clickedNewButton(self):
        print("ClickedNewButton")

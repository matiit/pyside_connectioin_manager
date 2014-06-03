from PySide.QtGui import *
from PySide.QtCore import Slot
from AddWindow import AddWindow
from DataRepository import DataRepository


class MainWindow(QDialog):

    # List of all connections
    data = []

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.newButton = QPushButton("Add new connection")
        self.listWidget = QListWidget(self)

        self.grid = QGridLayout()
        self.grid.addWidget(self.newButton, 0, 0)
        self.grid.addWidget(self.listWidget, 1, 0)

        self.setLayout(self.grid)

        self.newButton.clicked.connect(self.clickedNewButton)
        self.getData()
        self.addDataToList()

    def closeEvent(self, event):
        try:
            self.addWindowObj.close()
        except AttributeError:
            pass
        finally:
            event.accept()

    def getData(self):
        dataRep = DataRepository()
        self.data = dataRep.getConnectionsArray()
        print(self.data)

    def addDataToList(self):
        self.listWidget.clear()
        for connRow in self.data:
            self.listWidget.addItem(connRow['name'])

    @Slot()
    def clickedNewButton(self):
        self.addWindowObj = AddWindow()
        self.addWindowObj.initUi()
        self.addWindowObj.finished.connect(self.onAddFinish)

    @Slot()
    def onAddFinish(self):
        print("Test")
        self.addDataToList()
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
        self.listWidget.itemDoubleClicked.connect(self.onListItemClicked)
        self.addDataToList()

    def getData(self):
        dataRep = DataRepository()
        self.data = dataRep.getConnectionsArray()

    def addDataToList(self):
        self.getData()
        self.listWidget.clear()
        for connRow in self.data:
            self.listWidget.addItem(connRow['name'])

    @Slot()
    def clickedNewButton(self):
        self.addWindowObj = AddWindow(self)
        self.addWindowObj.initUi()
        self.addWindowObj.accepted.connect(self.onAddFinish)

    @Slot()
    def onAddFinish(self):
        self.addDataToList()
        print("onAddFinish")

    @Slot()
    def onListItemClicked(self):
        print("ITEM CLICKED")

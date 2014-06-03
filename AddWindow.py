from PySide.QtGui import QGridLayout, QDialog, QLabel, QLineEdit, QSpinBox, QPushButton
from PySide import QtCore
from PySide.QtCore import Slot
from DataRepository import *

class AddWindow(QDialog):
    def __init__(self, parent=None):
        super(AddWindow, self).__init__(parent)
        self.setGeometry(QtCore.QRect(110, 40, 171, 160))

    def initUi(self):
        self.grid = QGridLayout()
        self.grid.addWidget(QLabel("Connection name"), 0, 0)
        self.grid.addWidget(QLabel("Username"), 2, 0)
        self.grid.addWidget(QLabel("Password"), 4, 0)
        self.grid.addWidget(QLabel("Hostname"), 6, 0)
        self.grid.addWidget(QLabel("Port"), 8, 0)
        self.connectionNameInput =  QLineEdit(self)
        self.grid.addWidget(self.connectionNameInput, 1, 0)
        self.userNameInput =  QLineEdit(self)
        self.grid.addWidget(self.userNameInput, 3, 0)
        self.passwordInput =  QLineEdit(self)
        self.grid.addWidget(self.passwordInput, 5, 0)
        self.hostnameInput =  QLineEdit(self)
        self.grid.addWidget(self.hostnameInput, 7, 0)
        self.portSpinBox =  QSpinBox(self)
        self.portSpinBox.setMinimum(1)
        self.portSpinBox.setMaximum(65535)
        self.portSpinBox.setValue(22)
        self.grid.addWidget(self.portSpinBox, 9, 0)
        self.addButton = QPushButton("Accept")
        self.grid.addWidget(self.addButton, 10, 0)
        self.setLayout(self.grid)

        self.addButton.clicked.connect(self.clickedAddButton)

        self.show()

    @Slot()
    def clickedAddButton(self):
        dataRep = DataRepository()
        host = self.hostnameInput.text()
        port = self.portSpinBox.value()
        pwd = self.passwordInput.text()
        login = self.userNameInput.text()
        name = self.connectionNameInput.text()
        dataRep.addConnection({
            'host':host,
            'port':port,
            'pwd':pwd,
            'login':login,
            'name':name
        })
        self.close()

    # def closeEvent(self, event):
    #     try:
    #         print ("closing addWindow")
    #     except AttributeError:
    #         pass
    #     finally:
    #         event.accept()
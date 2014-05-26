from PySide.QtGui import *
from PySide import QtCore


class AddWindow(QDialog):
    def __init__(self, parent=None):
        super(AddWindow, self).__init__(parent)
        self.setGeometry(QtCore.QRect(110, 40, 171, 160))

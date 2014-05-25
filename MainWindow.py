import PySide

from PySide.QtGui import *
from PySide.QtCore import Slot


class AddWindow(QDialog):
    def __init__(self, parent=None):
        super(AddWindow, self).__init__(parent)
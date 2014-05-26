import sys

from PySide.QtGui import QApplication

from MainWindow import MainWindow
# Create the application object
app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()
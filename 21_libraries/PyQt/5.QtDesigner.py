# Qt Designer 
# https://build-system.fman.io/qt-designer-download
# is a graphical tool for building Qt GUIs:
    
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

Form, Window = uic.loadUiType("5.dialog.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec()
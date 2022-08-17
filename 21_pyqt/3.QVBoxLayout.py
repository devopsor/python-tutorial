
# Layouts let you position GUI elements next to each other. 
# QVBoxLayout for instance arranges items vertically:

from PyQt6.QtWidgets import *

if __name__ == '__main__':
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(QPushButton('Top'))
    layout.addWidget(QPushButton('Bottom'))
    window.setLayout(layout)
    window.show()
    app.exec()


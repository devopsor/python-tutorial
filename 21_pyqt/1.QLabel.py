# PyQt is a GUI widgets toolkit. It is a Python interface for Qt, one of the most powerful, and popular cross-
# platform GUI library. PyQt was developed by RiverBank Computing Ltd. 
# The latest version of PyQt can be downloaded from its official website − riverbankcomputing.com

# PyQt API is a set of modules containing a large number of classes and functions. 
# While QtCore module contains non-GUI functionality for working with file and directory etc., 
# QtGui module contains all the graphical controls. 
# In addition, there are modules for working with XML (QtXml), SVG (QtSvg), and SQL (QtSql), etc.

from PyQt6.QtWidgets import *

if __name__ == '__main__':
    app = QApplication([])
    label = QLabel('Hello World!')
    label.show()
    app.exec()

    
# PyQt Signals let you react to user input such as mouse clicks. 
# A slot is a function that gets called when such an event occurs. 
# The file main.py in this directory shows this in action: When the user clicks a button, a popup appears:

from PyQt6.QtWidgets import *

if __name__ == '__main__':
    app = QApplication([])
    button = QPushButton('Click')

    def on_button_clicked():
        alert = QMessageBox()
        alert.setText('You clicked the button!')
        alert.exec()

    button.clicked.connect(on_button_clicked)
    button.show()
    app.exec()
    
# The code begins in the usual way. First, we import PyQt6 and create a QApplication:

# from PyQt6.QtWidgets import *
# app = QApplication([])

# Next, we create a button:

# button = QPushButton('Click')

# Then we define a function. It will be called when the user clicks the button. You can see that it shows an alert:

# def on_button_clicked():
#     alert = QMessageBox()
#     alert.setText('You clicked the button!')
#     alert.exec()
# And here is where signals and slots come into play: We instruct Qt to invoke our function by connecting it 
# to the .clicked signal of our button:

# button.clicked.connect(on_button_clicked)
# Finally, we show the button on the screen and hand control over to Qt:

# button.show()
# app.exec()
# For instructions how you can run this example yourself, please see here.

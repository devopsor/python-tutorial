from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtWidgets import QApplication

app = QApplication([])
engine = QQmlApplicationEngine()
engine.load("6.main.qml")
app.exec()
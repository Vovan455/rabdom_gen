from PyQt6.QtWidgets import (QMainWindow, QApplication, QLabel, QPushButton, QVBoxLayout, QWidget)
from PyQt6.QtCore import Qt
from random import randint

app = QApplication([])
win = QWidget()

win.setWindowTitle("число")

win.resize(400,200)



text_1 = QLabel("Перкможець")
text_number = QLabel("?")

button = QPushButton("Згенерувати")

main_linr = QVBoxLayout()

main_linr.addWidget(text_1, alignment=Qt.AlignmentFlag.AlignCenter)
main_linr.addWidget(text_number, alignment=Qt.AlignmentFlag.AlignCenter)
main_linr.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)

win.setLayout(main_linr)

def click():
    rand_number = randint(1,100)
    text_number.setText(str(rand_number))

button.clicked.connect(click)

win.show()
app.exec()
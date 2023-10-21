from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QRadioButton, QMessageBox
app = QApplication([])
winda = QWidget()
winda.setWindowTitle('Лотерея')
winda.move(300,150)
winda.resize(500, 500)

def win():
    vic = QMessageBox()
    vic.setText("Вірно! /nВи винрали гіроскутер")
    vic.exec_()

def lose():
    vic = QMessageBox()
    vic.setText("Програш")
    vic.exec_()

text = QLabel()
text.setText('В якому уроці канал ортимав золоту кнопку?')

but1 = QRadioButton()
but1.setText('2015')

but2 = QRadioButton()
but2.setText('2016')

but3 = QRadioButton()
but3.setText('2017')

but4 = QRadioButton()
but4.setText('2018')


LineV = QHBoxLayout()
LineH1 = QHBoxLayout()
LineH2 = QHBoxLayout()
LineV.addWidget(text, alignment= Qt.AlignCenter)

LineH1.addWidget(but1, alignment= Qt.AlignCenter)
LineH1.addWidget(but2, alignment= Qt.AlignCenter)

LineH2.addWidget(but3, alignment= Qt.AlignCenter)
LineH2.addWidget(but4, alignment= Qt.AlignCenter)

LineV.addLayout(LineH1)
LineV.addLayout(LineH2)


    

winda.setLayout(LineV)
but1.clicked.connect(win)
but2.clicked.connect(lose)
but3.clicked.connect(lose)
but4.clicked.connect(lose)
winda.show()
app.exec_()
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])
window = QWidget()
window.setWindowTitle('генератор')
window.move(100,100)
window.resize(400,200)
window.move(100,100)

def rand():
    text.setText("Переможець:")
    text2.setText(str(randint(1,100)))
text = QLabel()
text.setText("Натисни, щоб дізнатися переможця")

text2 = QLabel()
text2.setText("?")

but = QPushButton()
but.setText("згенерувати")

lineV = QVBoxLayout()
lineV.addWidget(text, alignment= Qt.AlignCenter)
lineV.addWidget(text2, alignment= Qt.AlignCenter)
lineV.addWidget(but, alignment= Qt.AlignCenter)
window.setLayout(lineV)

but.clicked.connect(rand)



window.show()
app.exec_()
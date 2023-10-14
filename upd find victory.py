from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])
window = QWidget()
window.setWindowTitle('Лотерея')
window.move(100,100)
window.resize(400,200)
window.move(100,100)
def rand():
    num1 = str(randint(1,9))
    num2 = str(randint(1,9))
    text3.setText(num1)
    text2.setText(num2)

    if num1 == num2:
        text.setText("Ви виграли")
    else:
        text.setText("Ви програли")


text = QLabel()
text.setText("Натисни, щоб взяти участь")

text2 = QLabel()
text2.setText("?")

text3 = QLabel()
text3.setText("?")

but = QPushButton()
but.setText("випробувати удачу")

lineV = QVBoxLayout()
lineV.addWidget(text, alignment= Qt.AlignCenter)
lineV.addWidget(text2, alignment= Qt.AlignCenter)
lineV.addWidget(text3, alignment= Qt.AlignCenter)
lineV.addWidget(but, alignment= Qt.AlignCenter)
window.setLayout(lineV)

but.clicked.connect(rand)


window.show()
app.exec_()
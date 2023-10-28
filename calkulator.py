from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit
app = QApplication([])
window = QWidget()
window.setWindowTitle('Калькулятор')
window.move(300,300)
window.resize(500, 500)

def suma1():
    global f1
    global dia 
    f1 = int(text.text())
    text.setText("")
    dia = 1

def minus1():
    global f1
    global dia 
    f1 = int(text.text())
    text.setText("")
    dia = 3

def dil1():
    global f1
    global dia 
    f1 = int(text.text())
    text.setText("")
    dia = 2

def mnosh1():
    global f1
    global dia 
    f1 = int(text.text())
    text.setText("")
    dia = 4
def one1():
    text.setText(text.text()+"1")

def two1(): 
    text.setText(text.text()+"2")

def three1():
    text.setText(text.text()+"3")

def four1():
    text.setText(text.text()+"4")

def five1():
    text.setText(text.text()+"5")

def six1():
    text.setText(text.text()+"6")

def seven1():
    text.setText(text.text()+"7")

def eight1():
    text.setText(text.text()+"8")

def nine1():
    text.setText(text.text()+"9")

def zero1():
    text.setText(text.text()+"0")

def equal1():
    f2 = int(text.text())
    if dia == 1:
        text.setText(str(f1+f2))
    if dia == 2:
        if f2 == 0:
            text.setText("error")
        text.setText(str(f1/f2))  
    if dia == 3:
        text.setText(str(f1-f2)) 
    if dia == 4:
        text.setText(str(f1*f2))
        

text = QLineEdit()

suma = QPushButton()
suma.setText("+")

minus = QPushButton()
minus.setText("-")

dil = QPushButton()
dil.setText("/")

mnosh = QPushButton()
mnosh.setText("*")

equal = QPushButton()
equal.setText("=")

one = QPushButton()
one.setText("1")

two = QPushButton()
two.setText("2")

three = QPushButton()
three.setText("3")

four = QPushButton()
four.setText("4")

five = QPushButton()
five.setText("5")

six = QPushButton()
six.setText("6")

seven = QPushButton()
seven.setText("7")

eight = QPushButton()
eight.setText("8")

nine = QPushButton()
nine.setText("9")

zero = QPushButton()
zero.setText("0")

vl = QVBoxLayout()
hl1 = QHBoxLayout()
hl2 = QHBoxLayout()
hl3 = QHBoxLayout()
hl4 = QHBoxLayout()
hl5 = QHBoxLayout()
hl6 = QHBoxLayout()


hl1.addWidget(text)

hl2.addWidget(suma)
hl2.addWidget(minus)
hl2.addWidget(dil)
hl2.addWidget(mnosh)
hl2.addWidget(equal)


hl3.addWidget(one)
hl3.addWidget(two)
hl3.addWidget(three)

hl4.addWidget(four)
hl4.addWidget(five)
hl4.addWidget(six)

hl5.addWidget(seven)
hl5.addWidget(eight)
hl5.addWidget(nine)

hl6.addWidget(zero)

vl.addLayout(hl1)
vl.addLayout(hl2)
vl.addLayout(hl3)
window.setLayout(vl)

suma.clicked.connect(suma1)
minus.clicked.connect(minus1)
dil.clicked.connect(dil1)
mnosh.clicked.connect(mnosh1)
one.clicked.connect(one1)
two.clicked.connect(two1)
three.clicked.connect(three1)
four.clicked.connect(four1)
five.clicked.connect(five1)
six.clicked.connect(six1)
seven.clicked.connect(seven1)
eight.clicked.connect(eight1)
nine.clicked.connect(nine1)
zero.clicked.connect(zero1)
equal.clicked.connect(equal1)

window.show()
app.exec_()
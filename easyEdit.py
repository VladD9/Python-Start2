from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QListWidget,QLabel, QLineEdit
import os
app = QApplication([])
window = QWidget()
window.setWindowTitle('Калькулятор')
window.move(300,300)
window.resize(700, 400)

but_dir = QPushButton("Папка")
but_left = QPushButton("Вліво")
but_right = QPushButton("Вправо")
but_mirow = QPushButton("Дзеркально")
but_blur = QPushButton("Різкість")
but_bw = QPushButton("Ч\Б")

lb_img = QLabel("Тут буде картинка")

list_w = QListWidget()

lineV1 = QVBoxLayout()
lineV2 = QVBoxLayout()

lineH1 = QHBoxLayout()
lineG = QHBoxLayout()

lineV1.addWidget(but_dir)
lineV1.addWidget(list_w)

lineH1.addWidget(but_left)
lineH1.addWidget(but_right)
lineH1.addWidget(but_mirow)
lineH1.addWidget(but_blur)
lineH1.addWidget(but_bw)

lineV2.addWidget(lb_img,95)
lineV2.addLayout(lineH1)
lineG.addLayout(lineV1,20)
lineG.addLayout(lineV2,80)

window.setLayout(lineG)

def filter(files, extension):
    result = []
    for filename in files:
        for e in extension:
            if filename.endswith(e):
                result.append(filename)
    return result

def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def showFilenameList():
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    chooseWorkdir()
    filenames = filter(os.listdir(workdir),extensions)
    list_w.clear()
    for filename in filenames:
        list_w.addItem(filename)

but_dir.clicked.connect(showFilenameList)

window.show()
app.exec_()



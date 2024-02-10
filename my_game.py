import sys
import random
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui',self)
        self.lines = list(open("base.txt","r",encoding="utf-8"))
        self.random_line = random.choice(self.lines)
        self.letters = list(self.random_line)

        self.word_1 = list[0]
        self.word_2 = list[1]
        self.word_3 = list[2]
        self.word_4 = list[3]
        self.word_5 = list[4]

        self.label_1.setText(str(self.word_1))
        self.label_1.setVisible(False)
        self.label_2.setText(str(self.word_2))
        self.label_2.setVisible(False)
        self.label_3.setText(str(self.word_3))
        self.label_3.setVisible(False)
        self.label_4.setText(str(self.word_4))
        self.label_4.setVisible(False)
        self.label_5.setText(str(self.word_5))
        self.label_5.setVisible(False)

        self.pushButton.clicked.connect(self.liter_1)
        
    def liter_1(self):
        if "a" in list:
            if "а" == self.word_1:
                self.label_1.setVisible(True)
            if "а" == list[1]:
                self.label_2.setVisible(True)
            if "а" == list[2]:
                self.label_3.setVisible(True)
            if "а" == list[3]:
                self.label_4.setVisible(True)
            if "а" == list[4]:
                self.label_5.setVisible(True)
        else:
            life -= 1
      

    
        
    

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())

import sys
import random
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

lines = list(open("base.txt","r"))
random_line = random.choice(lines)
letters = list(random_line)





class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui',self)
        self.lines = list(open("base.txt","r"))
        self.random_line = random.choice(lines)
        self.letters = list(random_line)
    def start_game(self):
          

    
        
    

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())

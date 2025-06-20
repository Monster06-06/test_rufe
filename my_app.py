from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)


from instr import * 
from second_win import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI() 
        self.connects()
        self.set_appear()
        self.show()


    def initUI(self):
        '''создает графические элементы'''
        self.btn_next = QPushButton(txt_next, self)
        self.hello_text = QLabel(txt_hello)
        self.instruction  = QLabel(txt_instruction)

        self.layout_line = QVBoxLayot()
        self.layout_line.addWidget(self.hello_text, alighmet = Qt.AligmnLeft)
        self.layout_line.addWidget(self.instruction, alighmet = Qt.AlignLeft)
        self.layout_line.addWidget(self.btn_next, alighmet = Qt.AlignCenter)
        self.setLayout(self.layout_line)

    def next_click(self):
        self.tw = TestWin()
        self.hide()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

app = QApplication([])
mw = MainWin()
app.exec_()          

    



                                

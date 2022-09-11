import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget ,QApplication
from PyQt5 import uic

class UI(QWidget):
    def __init__(self):
        self.start()
        self.set()
    
    def start(self):
        self.ui = uic.loadUi('calculator.ui')
        self.ui.show()

    def set(self):
            self.ui.nubmer0.clicked.connect(lambda: self.click(num = 0))
            self.ui.nubmer1.clicked.connect(lambda:self.click(num = 1))
            self.ui.nubmer2.clicked.connect(lambda:self.click(num = 2))
            self.ui.nubmer3.clicked.connect(lambda:self.click(num = 3))
            self.ui.nubmer4.clicked.connect(lambda:self.click(num = 4))
            self.ui.nubmer5.clicked.connect(lambda:self.click(num = 5))
            self.ui.nubmer6.clicked.connect(lambda:self.click(num = 6))
            self.ui.number7.clicked.connect(lambda:self.click(num = 7))
            self.ui.nubmer8.clicked.connect(lambda:self.click(num = 8))
            self.ui.nubmer9.clicked.connect(lambda:self.click(num = 9))
            self.ui.plus.clicked.connect(lambda:self.click('+'))
            self.ui.minus.clicked.connect(lambda:self.click('-'))
            self.ui.multi.clicked.connect(lambda:self.click('*'))
            self.ui.slash.clicked.connect(lambda:self.click('/'))
            self.ui.zapitaya.clicked.connect(lambda:self.click('.'))
            self.ui.equally.clicked.connect(lambda:self.answer())
            self.ui.delete_2.clicked.connect(lambda:self.delete())
            self.ui.delete_last.clicked.connect(lambda:self.delete_last())
    def delete_last(self):
        x = self.ui.label.text()
        x = x[:-1]
        self.ui.label.setText(x)
    def delete(self):
        self.ui.label.setText(str(0))
    def answer(self):        
        t = selfui.label.text()
        if '/0' in t:
            self.ui.label.setText('ERROR')
        else:
            number = eval(t)
            self.ui.label.setText(str(number))
    def click(self, num=0):
        self.display(text=num)

    def display(self,text='0'):
        t = self.ui.label.text()
        if t == '0':
            t = ''
        text = '%s%s' % (t,text)
        self.ui.label.setText(text)
if __name__ == '__main__':

    
    app = QApplication(sys.argv)
    qiWindow = UI()
    app.exec_()

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
"""
class QButton(QWidget):
    def __init__(self,button_no):
        QtGui.QWidget.__init__(self, None)
        self.button = QtGui.QPushButton('Button'+str(button_no), self)
        self.name=str(button_no)

        self.button.clicked.connect(self.make_calluser(self.name,button_no))
    def make_calluser(self, name,no):
        def calluser():
            self.button.setText('btn-'+str(no))
            text=lineEdit.e1.text()
            print int(text)
        return calluser

class LineEdit(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self, None)
        self.e1=QtGui.QLineEdit()
        self.e1.setMaxLength(20)
        self.e1.setAlignment(QtCore.Qt.AlignRight)
        self.e1.setFont(QtGui.QFont('Arial',20))
  
def demo_QButton():

    app = QtGui.QApplication(sys.argv)
    window=QtGui.QWidget()
    grid=QtGui.QGridLayout()
    
    global lineEdit
    lineEdit=LineEdit()

    grid.addWidget(lineEdit.e1,0,0)

    for i in range(0,4):
        tb = QButton(i)
        grid.addWidget(tb,i+4,0)
    

    
    window.setLayout(grid)
    window.setGeometry(200,200,0,0)
    window.setFixedSize(400,400)
    window.setWindowTitle('CaLCi-1707')
    window.show()
    
    sys.exit(app.exec_())

if __name__=='__main__':
    demo_QButton()
"""
class make_QButton(QWidget):
    def __init__(self,btn_no):
        QWidget.__init__(self,None)
        self.btn=QPushButton(str(btn_no),self)
        self.btn.clicked.connect(self.make_CallBack(btn_no))

    def make_CallBack(self,btn_no):
        def CallBack():
            self.btn.setText('I am '+str(btn_no))
        return CallBack


class make_LineEdit(QWidget):
    def __init__(self):

        self.line_edit=QLineEdit()
        self.line_edit.setMaxLength(20)
        self.line_edit.setAlignment(Qt.AlignRight)
        self.line_edit.setFont(QFont('Arial',15))

def window():
    app=QApplication(sys.argv)
    window=QWidget()

    lineEdit=make_LineEdit()
    vBox=QVBoxLayout()
    grid=QGridLayout()
    hBox1=QHBoxLayout()

    count=0
    for i in range(0,3):
        for j in range(0,3):
            count+=1
            number_btn=make_QButton(count)
            grid.addWidget(number_btn,i,j)
    hBox1.addLayout(grid)

    hBox2=QHBoxLayout()
    hBox2.addWidget(lineEdit.line_edit)

    vBox.addLayout(hBox2)
    vBox.addLayout(hBox1)

    window.setLayout(vBox)
    window.setWindowTitle('CaLCi-1707')
    window.show()
    app.exec_()

if __name__=='__main__':
    window() 
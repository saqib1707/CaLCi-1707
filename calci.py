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
class make_Button(QWidget):
    def __init__(self,btn_repr):
        QWidget.__init__(self,None)
        self.btn=QPushButton(btn_repr,self)
        self.btn.clicked.connect(self.make_CallBack(btn_repr))

    def make_CallBack(self,btn_repr):
        def CallBack():
            lineEdit.line_edit.setText(btn_repr)
            self.btn.setText('I am '+btn_repr)
        return CallBack
"""
class Operand(QWidget):
    def __init__(self):
        self.operand_button=QPushButton(self,)
        self.operand_button.clicked.connect(self.make_callback())

    def make_callback(self):
        def callback():
            lineEdit.setText()


        self.minus_button=QPushButton(self,'-')
        self.into_button=QPushButton(self,'x')
        self.divide_button=QPushButton(self,'/')
"""
class make_LineEdit(QWidget):
    def __init__(self):

        self.line_edit=QLineEdit()
        self.line_edit.setMaxLength(20)
        self.line_edit.setAlignment(Qt.AlignRight)
        self.line_edit.setFont(QFont('Arial',15))

def window():
    app=QApplication(sys.argv)
    window=QWidget()

    global lineEdit
    lineEdit=make_LineEdit()
    vBox_outer=QVBoxLayout()
    grid=QGridLayout()

    hBox_number_button=QHBoxLayout()
    vBox_operand_button=QVBoxLayout()

    hBox_button=QHBoxLayout()
    button_list=['+','-','x','/']
    count=0
    for i in range(0,3):
        for j in range(0,3):
            count+=1
            number_btn=make_Button(str(count))
            grid.addWidget(number_btn,i,j)
    hBox_number_button.addLayout(grid)

    for i in range(len(button_list)):
        operand_btn=make_Button(button_list[i])
        vBox_operand_button.addWidget(operand_btn)


    hBox_button.addLayout(hBox_number_button)
    hBox_button.addLayout(vBox_operand_button)

    hBox_lineEdit=QHBoxLayout()
    hBox_lineEdit.addWidget(lineEdit.line_edit)

    vBox_outer.addLayout(hBox_lineEdit)
    vBox_outer.addLayout(hBox_button)

    window.setFixedSize(450,500)
    window.setLayout(vBox_outer)
    window.setWindowTitle('CaLCi-1707')
    window.show()
    app.exec_()

if __name__=='__main__':
    window() 
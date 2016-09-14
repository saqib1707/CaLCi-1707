import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import logicOfCalci

class make_Button(QWidget):
    def __init__(self,btn_repr):
        QWidget.__init__(self,None)
        self.btn=QPushButton(btn_repr,self)
        self.btn.clicked.connect(self.make_CallBack(btn_repr))

    def make_CallBack(self,btn_repr):
        def CallBack():
            lineEdit.line_edit.insert(btn_repr)
            #self.btn.setText('I am '+btn_repr)
            
        def result():
            global text
            text=lineEdit.line_edit.text()
            logicOfCalci.main(text)
        
        if btn_repr!='=':
            return CallBack
        else:
            return result

class make_LineEdit(QWidget):
    def __init__(self):

        self.line_edit=QLineEdit()
        self.line_edit.setMaxLength(40)
        self.line_edit.setAlignment(Qt.AlignRight)
        self.line_edit.setFont(QFont('Arial',15))

def window():
    app=QApplication(sys.argv)
    window=QWidget()

    global lineEdit
    lineEdit=make_LineEdit()
    vBox_outer=QVBoxLayout()
    grid=QGridLayout()
    answer_label=QLabel()
    answer_label.setAlignment(Qt.AlignRight)
    hBox_answerLabel=QHBoxLayout()
    hBox_answerLabel.addWidget(answer_label)

    button_list=[['+','<x','C'],['-','sqrt','pow'],['x','(',')'],['/','=','y']]
    another_list=[['0','.','%']]
    count=0
    for i in range(0,4):
        for j in range(0,3):
            if i!=3:
                count+=1
                number_btn=make_Button(str(count))
                grid.addWidget(number_btn,i,j)
            else:
                another_button=make_Button(another_list[0][j])
                grid.addWidget(another_button,i,j)

    for i in range(0,4):
        for j in range(3,6):
            operand_button=make_Button(button_list[i][j-3])
            grid.addWidget(operand_button,i,j)
    changeSlide_btn=make_Button('\/')
    grid.addWidget(changeSlide_btn,4,2)

    hBox_lineEdit=QHBoxLayout()
    hBox_lineEdit.addWidget(lineEdit.line_edit)

    vBox_outer.addLayout(hBox_answerLabel)
    vBox_outer.addLayout(hBox_lineEdit)
    vBox_outer.addLayout(grid)

    window.setGeometry(20,40,580,400)
    window.setLayout(vBox_outer)
    window.setWindowTitle('CaLCi-1707')
    window.show()
    app.exec_()

if __name__=='__main__':
    window() 
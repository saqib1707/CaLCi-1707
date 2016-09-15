import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import logicOfCalci
import math


#some constants

e=2.7
pi=math.pi
R=8.314
h=6.626e-34
k=1.38e-23
z=1
t=2


class make_Button(QWidget):
    def __init__(self,btn_repr):
        QWidget.__init__(self,None)
        self.btn=QPushButton(btn_repr,self)
        self.btn.clicked.connect(self.make_CallBack(btn_repr))

    def make_CallBack(self,btn_repr):
        def CallBack():
            lineEdit.line_edit.insert(btn_repr)
            
        def result():
            text=lineEdit.line_edit.text()
            final_result=logicOfCalci.main(text)
            answer_label.setText(str(final_result[0]))
        
        def clear():
            lineEdit.line_edit.clear()
        if btn_repr=='=':
            return result
        elif btn_repr=='C':
            return clear
        #elif btn_repr=='\/':
            #self.changeSlide()
        else:
            return CallBack
    #def changeSlide(self):

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
    grid_constants=QGridLayout()
    global answer_label
    answer_label=QLabel()
    answer_label.setAlignment(Qt.AlignRight)
    hBox_answerLabel=QHBoxLayout()
    hBox_answerLabel.addWidget(answer_label)

    button_list=[['+','<x','C'],['-','sqrt','pow'],['x','(',')'],['/','=','y']]
    another_list=[['0','.','%']]
    constants_list=['e','pi','R','h','k','t','z']
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

    for i in range(len(constants_list)):
        constants_btn=make_Button(constants_list[i])
        grid_constants.addWidget(constants_btn,0,i)
    
    hBox_lineEdit=QHBoxLayout()
    hBox_lineEdit.addWidget(lineEdit.line_edit)

    vBox_outer.addLayout(hBox_answerLabel)
    vBox_outer.addLayout(hBox_lineEdit)
    vBox_outer.addLayout(grid_constants)
    vBox_outer.addLayout(grid)

    window.setGeometry(20,40,580,550)
    window.setLayout(vBox_outer)
    window.setWindowTitle('CaLCi-1707')
    window.show()
    app.exec_()

if __name__=='__main__':
    window() 
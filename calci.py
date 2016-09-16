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
        self.btn.clicked.connect(self.make_CallBack())

    def make_CallBack(self):
        def CallBack():
            #lineEdit.line_edit.insert(btn_repr)
            lineEdit.line_edit.insert(self.btn.text())
            if self.btn.text() in ['sin()','cos()','tan()','log()','ln()','exp()','sqrt()']:
                txt=lineEdit.line_edit.text()
                lineEdit.line_edit.setCursorPosition(len(txt)-1)
            
        def result():
            text=lineEdit.line_edit.text()
            final_result=logicOfCalci.main(text)
            answer_label.setText(str(final_result[0]))
        
        def changeSlide():
            #print 'in <<< slide'
            if self.btn.text()=='>>>':
                changed_list=[['sin()','<x','C'],['cos()','log()','ln()'],['tan()','()','fan'],['zan','y','=']]
                for i in range(0,4):
                    for j in range(3,6):
                        abra=grid.itemAtPosition(i,j).widget()
                        abra.btn.setText(changed_list[i][j-3])
                
                grid.itemAtPosition(4,2).widget().btn.setText('<<<')
                #print self.btn.text()
            #self.btn.setText('>')
            elif self.btn.text()=='<<<':
                for i in range(0,4):
                    for j in range(3,6):
                        abra=grid.itemAtPosition(i,j).widget()
                        abra.btn.setText(button_list[i][j-3])
                grid.itemAtPosition(4,2).widget().btn.setText('>>>')

        def clear():
            lineEdit.line_edit.clear()
            answer_label.clear()

        if self.btn.text()=='=':
            return result
        elif self.btn.text()=='C':
            return clear
        elif self.btn.text()=='>>>':
            return changeSlide
        #elif self.btn.text()=='>':
            #return basicSlide
        else:
            #if btn_repr=='()':
                #lineEdit.line_edit.cursorBackward(False,1)
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

    global lineEdit,grid,vBox_outer
    lineEdit=make_LineEdit()
    vBox_outer=QVBoxLayout()
    grid=QGridLayout()
    grid_constants=QGridLayout()
    global answer_label
    answer_label=QLabel()
    answer_label.setAlignment(Qt.AlignRight)
    hBox_answerLabel=QHBoxLayout()
    hBox_answerLabel.addWidget(answer_label)

    global button_list
    button_list=[['+','<x','C'],['-','sqrt()','^'],['x','()','exp()'],['/','y','=']]
    another_list=[['0','.','%']]
    constants_list=['e','pi','R','h','k','t']
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
    changeSlide_btn=make_Button('>>>')
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
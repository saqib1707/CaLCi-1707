import sys,math,logicOfCalci
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class make_Button(QWidget):

    def __init__(self,btn_repr):				# btn_repr stands for button representation
        QWidget.__init__(self,None)
        self.button=QPushButton(btn_repr,self)
        self.button.setFixedSize(60,40)
        self.button.clicked.connect(self.make_CallBack())

    def make_CallBack(self):

        def writeToScreen():
            lineEdit.line_edit.insert(self.button.text())
            if self.button.text() in ['sin','cos','tan','log','ln','exp','sqrt']:
                txt=lineEdit.line_edit.text()
                lineEdit.line_edit.setCursorPosition(len(txt))
        
        def isNumber(s):
            try:
                float(s)
                return True
            except ValueError:
                return False

        def result():
            txt=lineEdit.line_edit.text()
            lineEdit.line_edit.setCursorPosition(len(txt))
            final_result,status=logicOfCalci.main(txt)
            try:
            	if status!='Successful':
            		if status=='':
            			answer_label.setText('Bad Expression')
            		else:
            			answer_label.setText(status)	
				# showing the integer result in integer form and floating type in decimal form
                elif isNumber(final_result[0]):
                	# for previous answer storage and storage
                    global prev_answer
                    prev_answer=final_result[0]

                    if math.floor(final_result[0])==final_result[0]:
                        answer_label.setText(str(int(final_result[0])))
                    else:
                        answer_label.setText(str(final_result[0]))
            except:
                answer_label.setText('Bad Expression')
        
        def advanceMode():
            if self.button.text()=='>>>':
                changed_list=[['sin','<x','C'],['cos','log','ln'],['tan','(','Ans'],['exp',')','=']]
                for i in range(1,5):
                    for j in range(3,6):
                        itemWidget=grid.itemAtPosition(i,j).widget()
                        itemWidget.button.setText(changed_list[i-1][j-3])
                
                grid.itemAtPosition(5,2).widget().button.setText('<<<')
        
            elif self.button.text()=='<<<':
                for i in range(1,5):
                    for j in range(3,6):
                        itemWidget=grid.itemAtPosition(i,j).widget()
                        itemWidget.button.setText(button_list[i-1][j-3])
                grid.itemAtPosition(5,2).widget().button.setText('>>>')

        def clear():
            lineEdit.line_edit.clear()
            answer_label.clear()

        def cutText():
            lineEdit.line_edit.backspace()
            if lineEdit.line_edit.text()=='':
                answer_label.clear()

        def lineInsert():
            global prev_answer
            lineEdit.line_edit.insert(str(prev_answer))

        if self.button.text()=='=':
            return result
        elif self.button.text()=='C':
            return clear
        elif self.button.text()=='>>>':
            return advanceMode
        elif self.button.text()=='<x':
            return cutText
        elif self.button.text()=='Ans':
            return lineInsert
        else:
            return writeToScreen

# making a class for making the text input field of calculator
class make_LineEdit(QWidget):
    def __init__(self):
        self.line_edit=QLineEdit()
        self.line_edit.setMaxLength(80)
        self.line_edit.setAlignment(Qt.AlignRight)
        self.line_edit.setFont(QFont('Arial',18))

def window():
    app=QApplication(sys.argv)
    window=QWidget()

    global lineEdit,grid,prev_answer
    prev_answer=0

    lineEdit=make_LineEdit()
    vBox_outer=QVBoxLayout()

    rect=QRect()
    rect.__init__(0,0,380,20)
    grid=QGridLayout()
    grid_constants=QGridLayout()
    grid_constants.setRowMinimumHeight(0,20)
    global answer_label
    answer_label=QLabel()
    answer_label.setAlignment(Qt.AlignRight)
    answer_label.setFixedSize(380,50)
    hBox_answerLabel=QHBoxLayout()
    hBox_answerLabel.addWidget(answer_label)

    global button_list

    # defining the buttons list...
    button_list=[['+','<x','C'],['-','sqrt','^'],['x','(','Ans'],['/',')','=']]
    another_list=[['0','.','%']]
    constants_list=['e','pi','R','h','k','t']

    # making of constants buttons in a separate grid layout 
    for i in range(len(constants_list)):
        constants_btn=make_Button(constants_list[i])
        grid.addWidget(constants_btn,0,i)
    
    # for making the basic initial numbers button which is not changed later
    count=0
    for i in range(1,5):
        for j in range(0,3):
            if i!=4:
                count+=1
                number_btn=make_Button(str(count))
                grid.addWidget(number_btn,i,j)
            else:
                another_button=make_Button(another_list[0][j])
                grid.addWidget(another_button,i,j)

    # for making the right sided dynamic operand buttons
    for i in range(1,5):
        for j in range(3,6):
            operand_button=make_Button(button_list[i-1][j-3])
            grid.addWidget(operand_button,i,j)

    # separately making the botton changing control button >>> and <<<
    changeSlide_btn=make_Button('>>>')
    grid.addWidget(changeSlide_btn,5,2)

    # adding the lineEdit widget in a Horizontal box
    hBox_lineEdit=QHBoxLayout()
    hBox_lineEdit.addWidget(lineEdit.line_edit)

    # finally adding all the layouts in the outer vertical box order wise
    vBox_outer.addLayout(hBox_answerLabel)
    vBox_outer.addLayout(hBox_lineEdit)
    vBox_outer.addLayout(grid)

    # setting the window properties
    window.setFixedSize(410,430)
    window.setLayout(vBox_outer)
    window.setBackgroundRole(QPalette.Base)
    window.setWindowTitle('CaLCi-1707')
    window.show()
    app.exec_()

if __name__=='__main__':
    window()

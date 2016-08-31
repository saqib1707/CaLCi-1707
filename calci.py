import sys
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui
#import math

#PI=Math.PI

class QButton(QtGui.QWidget):
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
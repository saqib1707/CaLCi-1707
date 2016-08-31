import sys
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui

class QButton(QtGui.QWidget):
    def __init__(self,button_no):
        QtGui.QWidget.__init__(self, None)
        self.button = QtGui.QPushButton('Button'+str(button_no), self)
        self.name=str(button_no)
        self.button.clicked.connect(self.make_calluser(self.name,button_no))
    def make_calluser(self, name,no):
        def calluser():
            self.button.setText('btn-'+str(no))
        return calluser
        
def demo_QButton():
    app = QtGui.QApplication(sys.argv)
    window=QtGui.QWidget()
    grid=QtGui.QGridLayout()
    for i in range(0,2):
        tb = QButton(i)
        grid.addWidget(tb,0,i)
    
    window.setLayout(grid)
    window.setGeometry(200,200,0,0)
    window.setFixedSize(400,400)
    window.setWindowTitle('CaLCi-1707')
    window.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    demo_QButton()
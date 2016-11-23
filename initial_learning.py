import sys	
from PyQt4.QtGui import *
from PyQt4.QtCore import *

#print dir(pygame)
"""
def window():
	app=QApplication(sys.argv)
	window=QDialog()
	global btn1
	btn1=QPushButton(window)
	btn1.setText('Button 1')
	btn1.clicked.connect(btn1_clicked)
	btn1.move(150,300)

	window.setGeometry(50,50,500,400)
	window.setWindowTitle("CaLci-1707")
	window.show()
	sys.exit(app.exec_())

def btn1_clicked():
	btn1.setText('Button clicked')

if __name__=='__main__':
	window()
"""

def changeButtonText(count):
	btn[count].setText('Hello')
	

def window():
	app=QApplication(sys.argv)
	window=QWidget()
	global btn
	btn=[]
	for i in range(0,4):
		for j in range(0,4):
			btn.append(QPushButton('Button'+str(i)+str(j)))
	"""
	vbox=QVBoxLayout()
	hbox=QHBoxLayout()
	hbox.addWidget(btn1)
	hbox.addStretch()
	hbox.addWidget(btn2)
	vbox.addLayout(hbox)
	window.setLayout(vbox)
	"""
	grid=QGridLayout()
	count=0
	for i in range(0,4):
		for j in range(0,4):
			grid.addWidget(btn[count],i,j)
			btn[count].clicked.connect(lambda:changeButtonText(count))
			count+=1

	window.setLayout(grid)
	window.setWindowTitle('CaLCi-1707')
	window.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	window()

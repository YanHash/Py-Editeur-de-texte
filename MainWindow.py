from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QObject, pyqtSignal
import sys


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self). __init__(parent)

def main(args):
	app = QApplication(args)
	win = MainWindow()
	win.resize(500,500)
	win.show()
	
	bar = win.menuBar() 
	
	fmenu = bar.addMenu("Fichier")
	
	act1 = QAction(QIcon("open.png"), "Open...", win)
	act2 = QAction(QIcon("save.png"), "Save...", win)
	act3 = QAction(QIcon("quit.png"), "Quit...", win)
	
	fmenu.addAction(act1)
	fmenu.addAction(act2)
	fmenu.addAction(act3)
	
	ftoolbar = win.addToolBar("Fichier")
	
	ftoolbar.addAction(act1)
	ftoolbar.addAction(act2)
	ftoolbar.addAction(act3)
	
	
	act1.setShortcut("Ctrl+O")
	act2.setShortcut("Ctrl+S")
	act3.setShortcut("Ctrl+Q")
	
	text = QTextEdit(win)
	win.setCentralWidget(text)
	
	#option
	win.statusBar().showMessage('Text Editor')
	
	
	fpath = None 

	
	@pyqtSlot(int)
	def openFile():
		global fpath
		path = QFileDialog.getOpenFileName(win, "Open")[0]
		if path:
			text.setPlainText(open(path).read())
			fpath = path
		
	act1.triggered.connect(openFile)
	act1.setShortcut(QKeySequence.Open)


	
	@pyqtSlot(int)
	def savefile() :
		path = QFileDialog.getSaveFileName(win, "Save")[0]
		with open(path, "w") as f:
			f.write(text.toPlainText())
			text.document().setModified(False)
		
	act2.triggered.connect(savefile)
	act2.setShortcut(QKeySequence.Save)
			
			
			
	@pyqtSlot(int)
	def quitApp() :
		msgbx = QMessageBox()
		msgbx.setText("Êtes-vous sûr de vouloir quitter ?")
		msgbx.setWindowTitle("QUITTER")
		msgbx.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
		returned = msgbx.exec_()
		if returned == QMessageBox.Ok :
			sys.exit()

		

	act3.triggered.connect(quitApp)
	act3.setShortcut(QKeySequence.Quit)
	
	
	app.exec_()


if __name__ == "__main__":
	print("execution du programme")
	main(sys.argv)



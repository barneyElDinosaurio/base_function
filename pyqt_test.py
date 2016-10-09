# -*-coding=utf-8-*-
__author__ = 'Rocky'

import sys
from PyQt4 import QtCore,QtGui,uic
qtCreatorFile="myUI.ui"
Ui_MainWindow,QtBaseClass= uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        print type(Ui_MainWindow)
        print type(QtBaseClass)
        self.getName.clicked.connect(self.showName)

    def showName(self):
        name=self.textEdit.toPlainText()
        if name =="" :
            print "Please input the name"
        else:
            print name
            self.display_line.setText(name)


def base_usage():
    app=QtGui.QApplication(sys.argv)
    w  =QtGui.QWidget()
    w.setWindowTitle("Rocky Title")
    w.show()
    sys.exit(app.exec_())
    #这样不会显示end
    print "End"


class ChangeUI_lable(QtGui.QWidget):
    def __init__(self,parent=None):
        super(ChangeUI_lable,self).__init__(parent)
        self.setWindowTitle("One")

        self.pushButton=QtGui.QPushButton("Rocky_Button")
        self.pushButton1=QtGui.QPushButton("Clear")
        self.textEdit=QtGui.QTextEdit()
        layout=QtGui.QVBoxLayout()

        self.pushButton.clicked.connect(self.onClick)
        self.pushButton1.clicked.connect(self.onClick1)

        layout.addWidget(self.textEdit)
        layout.addWidget(self.pushButton)
        layout.addWidget(self.pushButton1)
        self.setLayout(layout)
    def onClick(self):
        self.textEdit.setText("Click button")
    def onClick1(self):
        self.textEdit.setText("")

if __name__=="__main__":
    '''
    app=QtGui.QApplication(sys.argv)
    window=MyApp()
    window.show()
    sys.exit(app.exec_())
    '''
    #base_usage()
    app=QtGui.QApplication(sys.argv)
    w=ChangeUI_lable()
    w.show()
    sys.exit(app.exec_())
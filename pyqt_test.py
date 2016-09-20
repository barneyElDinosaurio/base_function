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

if __name__=="__main__":
    '''
    app=QtGui.QApplication(sys.argv)
    window=MyApp()
    window.show()
    sys.exit(app.exec_())
    '''
    base_usage()
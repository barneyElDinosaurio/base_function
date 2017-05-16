# -*-coding=utf-8-*-
from PyQt4.QtCore import QPointF, QLineF, Qt
from PyQt4.QtGui import QGraphicsLineItem, QGraphicsView, QGraphicsScene, QPen

__author__ = 'Rocky'

import sys
from PyQt4 import QtCore, QtGui, uic
# QGraphicsLineItem
#QGraphicsView
#QGraphicsScene
#QPointF
#QPen
#QLineF
qtCreatorFile = "myUI.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        print type(Ui_MainWindow)
        print type(QtBaseClass)
        self.getName.clicked.connect(self.showName)

    def showName(self):
        name = self.textEdit.toPlainText()
        if name == "":
            print "Please input the name"
        else:
            print name
            self.display_line.setText(name)


def base_usage():
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    w.setWindowTitle("Rocky Title")
    w.show()
    sys.exit(app.exec_())
    #这样不会显示end
    print "End"


class ChangeUI_lable(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ChangeUI_lable, self).__init__(parent)
        self.setWindowTitle("One")

        self.pushButton = QtGui.QPushButton("Rocky_Button")
        self.pushButton1 = QtGui.QPushButton("Clear")
        self.textEdit = QtGui.QTextEdit()
        layout = QtGui.QVBoxLayout()

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


class MyWidget(QGraphicsView):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setFixedSize(300, 300)
        self.setSceneRect(0, 0, 250, 250)
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.scene.addItem(MyArrow())


class MyArrow(QGraphicsLineItem):
    def __init__(self):
        super(MyArrow, self).__init__()
        self.source = QPointF(0, 250)
        self.dest = QPointF(120, 120)
        self.line = QLineF(self.source, self.dest)
        self.line.setLength(self.line.length() - 20)

    def paint(self, QPainter, QStyleOptionGraphicsItem, QWidget_widget=None):
        # setPen
        pen = QPen()
        pen.setWidth(5)
        pen.setJoinStyle(Qt.MiterJoin)  #让箭头变尖
        QPainter.setPen(pen)

        # draw line
        QPainter.drawLine(self.line)


class SigSlot(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setWindowTitle("Sig Slot Test")
        lcd = QtGui.QLCDNumber(self)
        slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(slider)

        self.setLayout(vbox)
        self.connect(slider, QtCore.SIGNAL('valueChanged(int)'), lcd, QtCore.SLOT('display(int)'))
        self.resize(250, 250)


class ProgressBar(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self)
        self.setGeometry(300, 300, 250, 150)

        self.pBar = QtGui.QProgressBar(self)
        self.pBar.setGeometry(30, 40, 200, 25)

        self.button = QtGui.QPushButton('start', self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(40, 80)

        self.connect(self.button, QtCore.SIGNAL('clicked()'), self.onStart)
        self.timer = QtCore.QBasicTimer()
        self.step = 0

    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            return
        self.step = self.step + 1
        self.pBar.setValue(self.step)

    def onStart(self):
        if self.timer.isActive():
            self.timer.stop()
            self.button.setText("Start")
        else:
            self.timer.start(100, self)
            self.button.setText(("Stop"))


class DrawTest(QtGui.QWidget):
    def __init__(self):
        pass


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    bar = ProgressBar()
    bar.show()
    sys.exit(app.exec_())

'''
if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())
'''

'''
if __name__=="__main__":

    app=QtGui.QApplication(sys.argv)
    window=MyApp()
    window.show()
    sys.exit(app.exec_())

    #base_usage()
    app=QtGui.QApplication(sys.argv)
    w=ChangeUI_lable()
    w.show()
    sys.exit(app.exec_())
'''
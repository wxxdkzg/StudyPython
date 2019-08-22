import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QApplication, QMainWindow
from HelloWorld import *

class MainWindowAPP(QtWidgets.QWidget, Ui_Form):   #   载入HelloWorld.py文件Ui_Form
    def __init__(self, parent=None):
        super(MainWindowAPP, self).__init__(parent)
        self.setupUi(self)
       # self.retranslateUi(self)

if __name__ == "__main__":
    #app = QtWidgets.QApplication(sys.argv)  #方法1
    app = QApplication(sys.argv)             #方法2，需要import QApplication
    myWin = MainWindowAPP()
    myWin.show()
    sys.exit(app.exec_())
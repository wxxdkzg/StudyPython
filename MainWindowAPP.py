import sys
from PyQt5.QtWidgets import  QApplication, QMainWindow, QMessageBox, QInputDialog
from MainWindow import *
from HelloWorld import *

class HelloAPP(QtWidgets.QWidget, Ui_Form):   #   载入HelloWorld.py文件Ui_Form
    def __init__(self, parent=None):
        super(HelloAPP, self).__init__(parent)
        self.setupUi(self)


class MainWindowAPP(QMainWindow, Ui_MainWindow):  #   载入MainWindow.py文件Ui_MainWindow
    def __init__(self, parent=None):
        super(MainWindowAPP, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.msgbox3)
        self.actionPage1.triggered.connect(self.msgbox1)
        self.actionPage2.triggered.connect(self.msgbox2)
        #显示、隐藏Hello窗口
        self.Hello = HelloAPP()
        self.actionopen.triggered.connect(self.helloShow)
        self.actionclose.triggered.connect(self.helloHide)

    def helloShow(self):
        self.gridLayout1.addWidget(self.Hello)
        self.Hello.show()
    def helloHide(self):
        #self.gridLayout1.addWidget(self.Hello)
        self.Hello.hide()

    def msgbox1(self):
        #print('test msgbox')
        #pass
        OK = QMessageBox.information(self,("信息框1"), ("""测试信息框1"""), QMessageBox.StandardButton(QMessageBox.Yes|QMessageBox.No))
    def msgbox2(self):
        i,okPressed = QInputDialog.getInt(self,("选择数字对话框"),("选择一个数字:"),50,0,100,1)
        #其它输入getDouble，getItem,getText
        if okPressed:
            print(i)
    def msgbox3(self):
        # Get item/choice
        items = ("Red", "Blue", "Green")
        item, okPressed = QInputDialog.getItem(self, "选择颜色对话框", "确定颜色：", items, 0, False)
        if okPressed and item:
            print(item)
    #其它类似如---QFileDialog：import QFileDialog 操作文件
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MainWindowAPP()
    myWin.show()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HelloWorld.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(380, 590)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(195, 39, 151, 31))
        self.textEdit.setObjectName("textEdit")
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(10, 210, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit.setGeometry(QtCore.QRect(130, 210, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.verticalSlider = QtWidgets.QSlider(Form)
        self.verticalSlider.setGeometry(QtCore.QRect(360, 20, 19, 160))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(170, 70, 171, 80))
        self.groupBox.setObjectName("groupBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 40, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(20, 20, 70, 17))
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 90, 151, 51))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 30, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(20, 10, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.fontComboBox = QtWidgets.QFontComboBox(Form)
        self.fontComboBox.setGeometry(QtCore.QRect(30, 170, 188, 22))
        self.fontComboBox.setObjectName("fontComboBox")
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 240, 321, 201))
        self.calendarWidget.setObjectName("calendarWidget")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 190, 361, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(143, 480, 20, 101))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 150, 381, 441))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/timgY51IEWAA.jpg"))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(190, 10, 113, 20))
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(30, 450, 131, 22))
        self.comboBox.setEditable(False)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox.setGeometry(QtCore.QRect(170, 450, 71, 22))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(250, 450, 71, 22))
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label.raise_()
        self.textEdit.raise_()
        self.dateEdit.raise_()
        self.dateTimeEdit.raise_()
        self.verticalSlider.raise_()
        self.groupBox.raise_()
        self.frame.raise_()
        self.fontComboBox.raise_()
        self.calendarWidget.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.lineEdit.raise_()
        self.comboBox.raise_()
        self.doubleSpinBox.raise_()
        self.spinBox.raise_()
        self.label_2.raise_()

        self.retranslateUi(Form)
        self.radioButton_2.clicked.connect(self.checkBox_2.toggle)
        self.calendarWidget.clicked['QDate'].connect(self.dateEdit.setDate)
        self.calendarWidget.clicked['QDate'].connect(self.dateTimeEdit.setDate)
        self.verticalSlider.sliderMoved['int'].connect(self.spinBox.setValue)
        self.comboBox.activated['QString'].connect(self.textEdit.append)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.textEdit, self.verticalSlider)
        Form.setTabOrder(self.verticalSlider, self.radioButton)
        Form.setTabOrder(self.radioButton, self.radioButton_2)
        Form.setTabOrder(self.radioButton_2, self.checkBox)
        Form.setTabOrder(self.checkBox, self.checkBox_2)
        Form.setTabOrder(self.checkBox_2, self.fontComboBox)
        Form.setTabOrder(self.fontComboBox, self.dateEdit)
        Form.setTabOrder(self.dateEdit, self.dateTimeEdit)
        Form.setTabOrder(self.dateTimeEdit, self.calendarWidget)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "GroupBox"))
        self.checkBox_2.setText(_translate("Form", "CheckBox"))
        self.checkBox.setText(_translate("Form", "CheckBox"))
        self.radioButton_2.setText(_translate("Form", "RadioButton"))
        self.radioButton.setText(_translate("Form", "RadioButton"))
        self.comboBox.setItemText(0, _translate("Form", "New Item1"))
        self.comboBox.setItemText(1, _translate("Form", "New Item2"))
        self.comboBox.setItemText(2, _translate("Form", "New Item3"))
        self.label_2.setText(_translate("Form", "测试界面1"))

import image_rcc_rc

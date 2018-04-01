# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ctmtranslate.ui'
#
# Created: Thu Feb 01 12:03:10 2018
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("Translate&named"))
        MainWindow.resize(824, 624)
        self.setWindowIcon(QtGui.QIcon('icon.icon'))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout.addWidget(self.textEdit)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.verticalLayout_5.addWidget(self.comboBox)
        self.verticalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.radioButton = QtGui.QRadioButton(self.centralwidget)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.verticalLayout_3.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.verticalLayout_3.addWidget(self.radioButton_2)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.translateBtn = QtGui.QPushButton(self.centralwidget)
        self.translateBtn.setMinimumSize(QtCore.QSize(0, 100))
        self.translateBtn.setObjectName(_fromUtf8("translateBtn"))
        self.verticalLayout_4.addWidget(self.translateBtn)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.horizontalLayout.addWidget(self.textBrowser)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 824, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen1 = QtGui.QAction(MainWindow)
        self.actionOpen1.setObjectName(_fromUtf8("actionOpen1"))
        self.actionOpen2 = QtGui.QAction(MainWindow)
        self.actionOpen2.setObjectName(_fromUtf8("actionOpen2"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Translate&named", "Translate&named", None))
        self.comboBox.setItemText(0, _translate("Translate&named", "不命名", None))
        self.comboBox.setItemText(1, _translate("Translate&named", "驼峰命名", None))
        self.comboBox.setItemText(2, _translate("Translate&named", "下划线命名", None))
        self.radioButton.setText(_translate("Translate&named", "中文 to 英文", None))
        self.radioButton_2.setText(_translate("Translate&named", "英文 to 中文", None))
        self.translateBtn.setText(_translate("Translate&named", "Translate", None))
        self.actionOpen1.setText(_translate("Translate&named", "open1", None))
        self.actionOpen2.setText(_translate("Translate&named", "open2", None))

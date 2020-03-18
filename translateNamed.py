#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-1-31 12:00:44
# @Author  : Demoon (a_share@sina.com)
# @Link    :
# @Version : $Id$
# @title   :

import sys
import os
import json
#引入ui文件
import ctmui
#引入翻译模块
import transModel
from PyQt5 import  QtCore, QtWidgets, uic

#处理编码问题
# reload(sys)
# sys.setdefaultencoding('utf-8')

#ui文件运用方法
#qtCreatorFile = os.path.join(os.getcwd(), os.path.splitext(os.path.basename(__file__))[0] +".ui")  # Enter file here.
#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
#ui转为py运用方法
Ui_MainWindow = ctmui.Ui_MainWindow

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.translateBtn.clicked.connect(self.translate)

    def translate(self):
        fromL = 'en'
        toL = 'zh'
        connect = self.textEdit.toPlainText()
        select = self.comboBox.currentIndex()
        if self.radioButton.isChecked():
            fromL = 'zh'
            toL = 'en'
        res = transModel.bdTrans(str(connect), fromL, toL)
        showStr = u'翻译失败！'
        if res['state'] is True:
            resDict = json.loads(res['connect'])

            if 'trans_result' in resDict:
                if self.radioButton.isChecked() and select != 0:
                    showStr = strNamed(resDict['trans_result'][0]['dst'], select)
                else:
                    showStr = resDict['trans_result'][0]['dst']
        self.textBrowser.setText(showStr)

def strNamed(words, namedType):
    newWords = words.lower()
    #驼峰命名
    if namedType == 1:
        newWords = newWords.lower()[0] + newWords.title()[1:]
        newWords = newWords.replace(' ','')
    elif namedType == 2:
        newWords = newWords.replace(' ','_')
    return newWords

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

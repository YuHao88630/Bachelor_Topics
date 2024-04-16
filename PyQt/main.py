# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import threading
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    @staticmethod
    def click_gowork():
        MainWindow.hide()
        
        os.system("cd /home/pi/face-recognition-ncs && python3 on.py --detector face_detection_model \--embedding-model face_embedding_model/openface_nn4.small2.v1.t7 \--recognizer output/recognizer.pickle \--le output/le.pickle")
        
        MainWindow.show()
        #print("gowork")
    @staticmethod
    def click_offwork():
        MainWindow.hide()
        os.system("cd /home/pi/face-recognition-ncs && python3 off.py --detector face_detection_model \--embedding-model face_embedding_model/openface_nn4.small2.v1.t7 \--recognizer output/recognizer.pickle \--le output/le.pickle")
        MainWindow.show()
        #print("offwork")
    @staticmethod
    def click_takepic():
        MainWindow.hide()
        os.system("python3 add.py")
        MainWindow.show()
        #print('555')
    
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(846, 594)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 255);"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 100, 271, 211))
        self.label.setStyleSheet("image:url(/home/pi/Desktop/resource/camera.png)")
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 271, 211))
        self.label_2.setStyleSheet(_fromUtf8("image: url(/home/pi/Desktop/resource/clock (2).png);"))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(560, 100, 271, 211))
        self.label_3.setStyleSheet(_fromUtf8("image: url(/home/pi/Desktop/resource/user.png);"))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 350, 141, 81))
        self.pushButton.setStyleSheet(_fromUtf8("font: 22pt \"微軟正黑體\";\n"
"background-color: rgb(234, 234, 234);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.click_gowork)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 450, 141, 81))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(234, 234, 234);\n"
"font: 75 22pt \"微軟正黑體\";"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.click_offwork)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 400, 141, 81))
        self.pushButton_3.setStyleSheet(_fromUtf8("background-color: rgb(234, 234, 234);\n"
"font: 75 22pt \"微軟正黑體\";"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(630, 400, 141, 81))
        self.pushButton_4.setStyleSheet(_fromUtf8("background-color: rgb(234, 234, 234);\n"
"font: 22pt \"微軟正黑體\";"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.clicked.connect(self.click_takepic)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 0, 321, 81))
        self.label_4.setStyleSheet(_fromUtf8("font: 75 36pt \"微軟正黑體\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 846, 28))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.pushButton.setText(_translate("MainWindow", "上班打卡", None))
        self.pushButton_2.setText(_translate("MainWindow", "下班打卡", None))
        self.pushButton_3.setText(_translate("MainWindow", "重拍頭貼", None))
        self.pushButton_4.setText(_translate("MainWindow", "新增頭貼", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">主頁面</span></p></body></html>", None))
    
        
#import source_rc
if __name__=="__main__":
    lock=threading.Lock()
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
    
    
    
    
    
    


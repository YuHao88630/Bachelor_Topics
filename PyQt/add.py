# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!
import requests
from PyQt5 import QtCore,QtWidgets
import sys
import os
import json
from urllib import request
#import pandas as pd
#import os
from picamera import PiCamera
import shutil
import sqlite3
import time
import cv2
from imutils import paths
import numpy as np
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





class Ui_Dialog(object):
    @staticmethod
    def getEmployeeInfo(number):
        
          
        '''url = "https://dpy02.herokuapp.com/api/employee/?format=json"
        req = request.Request(url, headers)
        json_data = request.urlopen(req).read().decode("utf-8")
        json_data = json.loads(json_data);'''
        
        url = "https://dpy02.herokuapp.com/api/employee/?format=json"

        payload={}
        files={}
        headers = {
          'Authorization': 'Basic SkFZOjEyMzQ1Njc4OQ=='
        }

        response = requests.request("GET", url, headers=headers, data=payload, files=files)
        dict={}
        for item in response:
            if item['number']==number:
                dict=item
                break
        return dict
    @staticmethod
    def click_pic1(label):
        label.setText("aaa")
    @staticmethod
    def click_pic(self,textEdit,label):
        newNumber=textEdit.toPlainText()
        path='/home/pi/face-recognition-ncs/dataset/%s'% (newNumber)
        
        url = "https://dpy02.herokuapp.com/api/employee/?format=json"

        payload={}
        files={}
        headers = {
          'Authorization': 'Basic SkFZOjEyMzQ1Njc4OQ=='
        }

        response = requests.request("GET", url, headers=headers, data=payload, files=files)

        

        
        
        #json_data = request.urlopen(req).read().decode("utf-8")
        #json_data = json.loads(json_data)
        print(response.text)
        print(files)
        dict={}
        response=response.json()
        
        for item in response:
            if item["number"]==newNumber:
                dict=item
                break
        
        
        
        if(os.path.isdir(path) or bool(dict)==False):
            label.setText("ERROR!!Please key in your number again.")
            #self.reStart
            
            '''newNumber=textEdit.toPlainText()
            path='/home/pi/face-recognition-ncs/dataset/%s'% (newNumber)
            url = "http://192.168.2.11:8000/api/employee/?format=json"
            json_data = request.urlopen(url).read().decode("utf-8")
            json_data = json.loads(json_data)
            dict={}
            for item in json_data:
                if item['number']==newNumber:
                    dict=item
                    break'''
            
            
            #rely=QtWidgets.QMessageBox.warning(self,"Error","ERROR!!Please key in your number again.",QMessageBox.Yes)
            #self.label_3.setText("EXIST!!Please key in your number again.")
            #print("EXIST!!Please key in your number again.")
            
            
        else:
            Dialog.hide()
            
            #os.mkdir(newNumber)
            #os.mkdir('dataSingle')
            #os.chmod('dataSingle', mode=0o777)
            path='/home/pi/face-recognition-ncs/dataset/dataSingle/%s'% (newNumber)
            os.system("cd /home/pi/face-recognition-ncs/dataset/ && sudo rm -r dataSingle")
            os.system("cd /home/pi/face-recognition-ncs/dataset && mkdir dataSingle")
            os.system("cd /home/pi/face-recognition-ncs/dataset/ && mkdir %s"%(newNumber))
            os.system("cd /home/pi/face-recognition-ncs/dataset/dataSingle && mkdir %s"%(newNumber))
            #os.makedirs(path)
            camera=PiCamera()
            camera.resolution=(1440,1080)
            camera.framerate=15
            camera.start_preview()
            camera.brightness=55
            for i in range(10):
                time.sleep(2)
                camera.capture('/home/pi/face-recognition-ncs/dataset/%s/image%s.png'% (newNumber,i))
                p='/home/pi/face-recognition-ncs/dataset/%s/image%s.png'% (newNumber,i)
                shutil.copy(p,path)
            imagePaths = list(paths.list_images('/home/pi/face-recognition-ncs/dataset/dataSingle'))
            for i in range(len(imagePaths)):
                image=cv2.imread(imagePaths[i])
                path,name=os.path.split(imagePaths[i])
                #print(path)
                #print(name)
                name=name.split('.')[0]
                #print(name)
                (B,G,R) = cv2.split(image)
                gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
                B=cv2.resize(B,(480,360))
                G=cv2.resize(G,(480,360))
                R=cv2.resize(R,(480,360))
                gray=cv2.resize(gray,(480,360))
                cv2.imwrite(os.path.join(path,'{}GRAY.png'.format(name)),gray)
                cv2.imwrite(os.path.join(path,'{}B.png'.format(name)),B)
                cv2.imwrite(os.path.join(path,'{}G.png'.format(name)),G)
                cv2.imwrite(os.path.join(path,'{}R.png'.format(name)),R)
                bH = cv2.equalizeHist(B)
                gH = cv2.equalizeHist(G)
                rH = cv2.equalizeHist(R)
                result = cv2.merge((bH, gH, rH))
                cv2.imwrite(os.path.join(path,'{}.png'.format(name)),result)

            camera.stop_preview()


            #empDict=getEmployeeInfo(newNumber)
            #con = sqlite3.connect('employee.db')
            #cursorObj = con.cursor()
            #sql="""INSERT INTO employee(name,number,depart,position) VALUES(?,?,?,?)"""
            #data_tuple = (empDict['name'],empDict['number'],empDict['depart'],empDict['position'])
            #print(data_tuple)
            #cursorObj.execute(sql,data_tuple)
            #cursorObj.execute("""INSERT INTO employee(name,number,depart,position) VALUES("a","b","c","d")""")
            #con.commit()
            #cursorObj.close()
            #os.system("cd /home/pi/face-recognition-ncs && python align_faces.py -r /home/pi/face-recognition-ncs/dataset/%s -d /home/pi/face-recognition-ncs/dataset/%s"% (newNumber,newNumber))
            os.system("cd /home/pi/face-recognition-ncs && python3 extract_embeddings_Single.py \--dataset /home/pi/face-recognition-ncs/dataset/dataSingle  \--embeddings output/embeddings.pickle \--detector face_detection_model \--embedding-model face_embedding_model/openface_nn4.small2.v1.t7")
            os.system("cd /home/pi/face-recognition-ncs && python3 train_model.py --embeddings output/embeddings.pickle \--recognizer output/recognizer.pickle --le output/le.pickle")
        

    @staticmethod
    def click_return():
        
        Dialog.close()

    def reStart():
        Dialog.close()
        os.system("python3 add.py")
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(693, 524)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 255);"))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 30, 511, 141))
        self.label.setStyleSheet(_fromUtf8("font: 75 48pt \"微軟正黑體\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(120, 240, 441, 41))
        self.textEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 360, 171, 91))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(234, 234, 234);\n"
"font: 75 28pt \"微軟正黑體\";"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(lambda:self.click_pic(self,self.textEdit,self.label_3))#click2
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 360, 171, 91))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(234, 234, 234);\n"
"font: 75 28pt \"微軟正黑體\";"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.click_return)#click1
        
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(120, 200, 201, 22))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(120, 290, 271, 41))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">新增員工大頭貼</span></p></body></html>", None))
        self.pushButton.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">確定</span></p></body></html>", None))
        self.pushButton.setText(_translate("Dialog", "開啟", None))
        self.pushButton_2.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">確定</span></p></body></html>", None))
        self.pushButton_2.setText(_translate("Dialog", "上一頁", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Please type your number</span></p></body></html>", None))
if __name__=="__main__":
    #lock=threading.Lock()
    app=QtWidgets.QApplication(sys.argv)
    Dialog=QtWidgets.QMainWindow()
    ui=Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

import json
from urllib import request
#import pandas as pd
import os
from picamera import PiCamera
import shutil
import sqlite3
import time
import cv2
from imutils import paths
import numpy as np
def getEmployeeInfo(number):

	url = "http://192.168.2.9:8000/api/employee/?format=json"
	json_data = request.urlopen(url).read().decode("utf-8")
	json_data = json.loads(json_data);
	dict={}
	for item in json_data:
		if item['number']==number:
			dict=item
			break
	return dict
newNumber=input("Please key in your number")
while(os.path.isdir(newNumber)):
	newNumber=input("EXIST!!Please key in your number again.")
	while(getEmployeeInfo(newNumber)==False):
		newNumber=input("NUMBER NOT FOUND!!Please key in your number again.")
os.mkdir(newNumber)
os.mkdir('dataSingle')
#os.chmod('dataSingle', mode=0o777)
path='/home/pi/face-recognition-ncs/dataset/dataSingle/%s'% (newNumber)
os.system("cd /home/pi/face-recognition-ncs/dataset/dataSingle && mkdir %s"%(newNumber))
#os.makedirs(path)
camera=PiCamera()
camera.resolution=(1440,1080)
camera.framerate=15
camera.start_preview()
camera.brightness=55
for i in range(4):
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
os.system("cd /home/pi/face-recognition-ncs && python extract_embeddings_Single.py \--dataset /home/pi/face-recognition-ncs/dataset/dataSingle  \--embeddings output/embeddings.pickle \--detector face_detection_model \--embedding-model face_embedding_model/openface_nn4.small2.v1.t7")
os.system("cd /home/pi/face-recognition-ncs && python train_model.py --embeddings output/embeddings.pickle \--recognizer output/recognizer.pickle --le output/le.pickle")
os.system("cd /home/pi/face-recognition-ncs/dataset/ && sudo rmdir dataSingle")


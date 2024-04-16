import json
from urllib import request
#import pandas as pd
import os
from picamera import PiCamera
import shutil
import sqlite3
import time
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

camera=PiCamera()
camera.resolution=(1440,1080)
camera.framerate=15
camera.start_preview()
camera.brightness=55
for i in range(4):
	time.sleep(2)
	camera.capture('/home/pi/face-recognition-ncs/dataset/%s/image%s.png'% (newNumber,i))
	
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
os.system("cd /home/pi/face-recognition-ncs && python extract_embeddings.py \--dataset dataset  \--embeddings output/embeddings.pickle \--detector face_detection_model \--embedding-model face_embedding_model/openface_nn4.small2.v1.t7")
os.system("cd /home/pi/face-recognition-ncs && python train_model.py --embeddings output/embeddings.pickle \--recognizer output/recognizer.pickle --le output/le.pickle")



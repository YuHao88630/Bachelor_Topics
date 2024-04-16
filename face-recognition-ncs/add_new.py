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
newNumber=input("Please key in your number")
while(os.path.isdir(newNumber)):
	newNumber=input("EXIST!!Please key in your number again.")
	


#os.chmod('dataSingle', mode=0o777)
path='/home/pi/face-recognition-ncs/dataset/%s'% (newNumber)
os.system("cd /home/pi/face-recognition-ncs/dataset/ && mkdir %s"%(newNumber))
#os.makedirs(path)
camera=PiCamera()
camera.resolution=(1440,1080)
camera.framerate=15
camera.start_preview()
#camera.brightness=40
for i in range(4):
	time.sleep(2)
	camera.capture('/home/pi/face-recognition-ncs/dataset/%s/image%s.png'% (newNumber,i))
	#p='/home/pi/face-recognition-ncs/dataset/%s/image%s.png'% (newNumber,i)
	


camera.stop_preview()

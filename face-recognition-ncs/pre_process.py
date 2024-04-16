import numpy as np
import cv2
from imutils import paths
import os
#image = cv2.imread("")

#cv2.imshow("Original",image)
imagePaths = list(paths.list_images('/home/pi/face-recognition-ncs/dataset_new'))
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
	#cv2.imwrite(os.path.join(path,'{}BH.jpg'.format(name)),bH)
	#cv2.imwrite(os.path.join(path,'{}GH.jpg'.format(name)),gH)
	#cv2.imwrite(os.path.join(path,'{}RH.jpg'.format(name)),rH)
	
	
	
	'''(B,G,R) = cv2.split(image)
	
	cv2.imwrite("C:\\Users\\JUN-HONG\\Dropbox\\face-recognition-ncs\\dataset\\abhishek\\00000G.jpg",G)
	cv2.imwrite("C:\\Users\\JUN-HONG\\Dropbox\\face-recognition-ncs\\dataset\\abhishek\\00000R.jpg",R)
bH = cv2.equalizeHist(B)
gH = cv2.equalizeHist(G)
rH = cv2.equalizeHist(R)
cv2.imshow("Red",R)
cv2.imshow("Green",G)
cv2.imshow("Blue",B)
#cv2.waitKey(0)

result = cv2.merge((bH, gH, rH))
#cv2.imshow("dst", result)
cv2.imwrite("C:\\Users\\JUN-HONG\\Dropbox\\face-recognition-ncs\\dataset\\abhishek\\00000H.jpg",result)
cv2.imwrite("C:\\Users\\JUN-HONG\\Dropbox\\face-recognition-ncs\\dataset\\abhishek\\00000BH.jpg",bH)
cv2.imwrite("C:\\Users\\JUN-HONG\\Dropbox\\face-recognition-ncs\\dataset\\abhishek\\00000GH.jpg",gH)
cv2.imwrite("C:\\Users\\JUN-HONG\\Dropbox\\face-recognition-ncs\\dataset\\abhishek\\00000RH.jpg",rH)'''

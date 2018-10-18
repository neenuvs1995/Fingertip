import cv2   
import numpy as np

#capturing video through webcam
cap=cv2.VideoCapture(0)

while(1):
	_, img = cap.read()
	    
	#converting frame(img i.e BGR) to HSV (hue-saturation-value)

	hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	#defining the Range of Blue color
	blue_lower=np.array([99,115,150],np.uint8)
	blue_upper=np.array([110,255,255],np.uint8)
	#finding the range of red,blue and yellow color in the image
	
	blue=cv2.inRange(hsv,blue_lower,blue_upper)
	#Morphological transformation, Dilation  	
	kernal = np.ones((5 ,5), "uint8")
	blue=cv2.dilate(blue,kernal)
	res1=cv2.bitwise_and(img, img, mask = blue)
			
	#Tracking the Blue Color
	(_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>300):
			x,y,w,h = cv2.boundingRect(contour)	
			img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
			cv2.putText(img,"Blue color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))


            
           
    	



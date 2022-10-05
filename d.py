# drawing on top of images and shapes and stuff

from email.mime import image
import cv2
import numpy as np

# Create a blank image
img=np.zeros((512,512,3),np.uint8)
img[:]=255,255,255

# Draw some shapes 

# Image,centerpoint,radius,color,thickness
cv2.circle(img,(256,256),150,(0,69,255),cv2.FILLED)

# Image,point1,point4,color,thickness
cv2.rectangle(img,(130,226),(382,286),(255,255,255),cv2.FILLED)

# Image,pt1,pt2,color,thickness
cv2.line(img,(130,296),(382,296),(0,0,0),2)

# Image,text,startlinr,font,scale,color,thickness
cv2.putText(img,"Hehehe",(137,262),cv2.FONT_HERSHEY_SIMPLEX,0.75,(0,69,255),2)


cv2.imshow("Img",img)
cv2.waitKey(0)

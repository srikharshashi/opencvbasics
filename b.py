# Basic Image Processing

import cv2
import numpy as np

img=cv2.imread('barney.png')

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Kernel Size needs to be given to blur the image
imgBlur=cv2.GaussianBlur(img,(9,9),2) 

# Find Edges 
imgCanny=cv2.Canny(img,100,150)

# Dilation - increase thickness of images
# kernel is a numpy array
kerneld=np.ones((5,5),np.uint8)
imgDia=cv2.dilate(imgCanny,kerneld,iterations=1)


# Erosion - cecreaese the width of edges
imgEro=cv2.erode(imgDia,kerneld,iterations=3)

cv2.imshow("original",img)
cv2.imshow("greyscale",imgGray)
cv2.imshow("blur",imgBlur)
cv2.imshow("Canny",imgCanny)
cv2.imshow("Dilate",imgDia)
cv2.imshow("Erode",imgEro)

cv2.waitKey(0)
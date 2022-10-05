# Resizing and Cropping Images

import cv2
import numpy as np

img=cv2.imread('barney.png')

# Heigth,width,no of channels
# OpenCV - uses BGR
print(img.shape) 

# Resize by pixels
imgResize1=cv2.resize(img,(300,300))

# Resize by Scale
imgResize2=cv2.resize(img,(0,0),None,0.8,0.8)

# Cropping Images 
# Cropping Images is simple as it is just slicing them as matrices 
# OpenCV img objects are numpy arrays

imgCrop=img[100:200,300:400]



cv2.imshow("Image",img)
cv2.imshow("Resized 1",imgResize1)
cv2.imshow("Resized 2",imgResize2)
cv2.imshow("Cropped",imgCrop)



cv2.waitKey(0)
# Very Basic stuff

import cv2



# Read an Image

# img=cv2.imread("ss.png")
# cv2.imshow("Output",img)
# cv2.waitKey(0)

# Read and show a video
# Based upon the number of frames per second we get n*(time in seconds) number of images

# frameWidth=640
# frameHeight=480
# cap=cv2.VideoCapture('vid.mp4')
# while True:
#     success,img =cap.read()
#     img=cv2.resize(img,(frameWidth,frameHeight))
#     cv2.imshow("OP",img)
#     if cv2.waitKey(1) & 0xFF==ord('q'):
#         break
    
    
# Using the Webcam

# frameWidth=640
# frameHeight=480
# # Replace VideoCapture Source to webcam
# cap=cv2.VideoCapture(0)
# while True:
#     success,img =cap.read()
#     img=cv2.resize(img,(frameWidth,frameHeight))
#     cv2.imshow("OP",img)
#     if cv2.waitKey(1) & 0xFF==ord('q'):
#         break



    
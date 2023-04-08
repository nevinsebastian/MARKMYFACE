import os

import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackgrund = cv2.imread('Resources/background.png')


folderModePath = 'Resources/Modes'         # sets the path to the folder containing the images
modePathList = os.listdir(folderModePath)    # gets a list of all the files in the folder
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))  # reads the image at the path and appends it to the imgModeList
print(len(imgModeList))

while True:
    success, img = cap.read()

    imgBackgrund[162:162+480,55:55+640] = img #adjest the image

    #cv2.imshow("webcam", img)
    cv2.imshow("Face Attendance", imgBackgrund) #to overlay webcam live strame to the background.png
    cv2.waitKey(1)

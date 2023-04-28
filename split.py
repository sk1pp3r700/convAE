##code by OG_skipper


import cv2
import numpy as np
import os

# video from same folder:
cap = cv2.VideoCapture('insert name of video here with extension')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: making folder for data')

currentFrame = 0
while(True):
    # Capturing frame-by-frame
    ret, frame = cap.read()

    # for saving image of the current frame in jpg file
    name = './data/frame' + str(currentFrame) + '.jpg'
    print ('making..' + name)
    cv2.imwrite(name, frame)

    # for stopping duplicating images
    currentFrame += 1

# When done, close
cap.release()
cv2.destroyAllWindows()
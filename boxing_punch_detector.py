import cv2
import mediapipe as mp 
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# VIDEO FEED
wCam, hCam = 1280, 720
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)



while(True):      
    # Capture the video frame by frame
    ret, frame = cap.read()
  
    # Display the resulting frame
    cv2.imshow('feed', frame)
      
    # the 'q' button is used to quit
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
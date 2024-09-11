import cv2
import mediapipe
import pyautogui


camera = cv2.VideoCapture(0) #have only 1 camera
while True:
     _, image = camera.read()
     cv2.imshow("Eye mouse" , image)
     key = cv2.waitKey(100)
     if key ==27: #escape key code
          break 
camera.release()
cv2.destroyAllWindows()
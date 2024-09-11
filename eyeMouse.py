import cv2
import mediapipe
import pyautogui
face_landmark = mediapipe.solutions.face_mesh.FaceMesh(refine_landmarks = True) #using mediapipe solutions and faceMesh to detect facial landmarks. reining it to make it more accurate in some areas

camera = cv2.VideoCapture(0) #have only 1 camera
while True:
     _, image = camera.read()
     window_height, window_width, _ = image.shape
     rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #converting to rgb format from bgr format
     processed_image = face_landmark.process(rgb_image) #processing the changed image 
     all_faces = processed_image.multi_face_landmarks #storing all landmarks of faces
     if all_faces:
          one_face = all_faces[0].landmark #getting landmark of one face, ie the first detected face
          for landmark_point in one_face:
               x = int(landmark_point.x * window_width) #changing the decimals according to window width and height 
               y = int(landmark_point.y * window_height) #using int
               print(x, y) 
               cv2.circle(image,(x,y),3,(0,0,225))
     cv2.imshow("Eye mouse" , image)
     key = cv2.waitKey(100)
     if key ==27: #escape key code
          break 
camera.release()
cv2.destroyAllWindows()
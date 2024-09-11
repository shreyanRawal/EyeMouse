import cv2
import mediapipe
import pyautogui
face_landmark = mediapipe.solutions.face_mesh.FaceMesh(refine_landmarks = True) #using mediapipe solutions and faceMesh to detect facial landmarks. reining it to make it more accurate in some areas

camera = cv2.VideoCapture(0) #have only 1 camera
screen_w , screen_h = pyautogui.size()

while True:
     _, image = camera.read()
     image = cv2.flip(image,1) #lipping image as it shows opposite, 1 for horizontal
     window_height, window_width, _ = image.shape
     rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #converting to rgb format from bgr format
     processed_image = face_landmark.process(rgb_image) #processing the changed image 
     all_faces = processed_image.multi_face_landmarks #storing all landmarks of faces
     if all_faces:
          one_face = all_faces[0].landmark #getting landmark of one face, ie the first detected face
          for id,landmark_point in enumerate(one_face[474:478]): #points number of eyes
               x = int(landmark_point.x * window_width) #changing the decimals according to window width and height 
               y = int(landmark_point.y * window_height) #using int
               # print(x, y) 
               if id ==1: #to track only one point out of 4, we can use others too 
                     mouse_x = int(screen_w / window_width * x) #getting x and y axis according to screen and window size
                     mouse_y = int(screen_h / window_height * y)
                     pyautogui.moveTo(mouse_x,mouse_y)

               cv2.circle(image,(x,y),3,(0,0,225))
          left_eye = [one_face[145],one_face[159]]  #getting points of left eye
          for landmark_point in left_eye: #same for let eye
               x = int(landmark_point.x * window_width) 
               y = int(landmark_point.y * window_height) 
               # print(x, y) 
               cv2.circle(image,(x,y),3,(0,0,10)) 
          if(left_eye[0].y - left_eye[1].y < 0.01): #checking if the eye is closed by the distance between 2 points
                     pyautogui.click() #to click
                     pyautogui.sleep(2) #to wait or 2 sec
                     print("mouse clicked")
        
     cv2.imshow("Eye mouse" , image)
     key = cv2.waitKey(100)
     if key ==27: #escape key code
          break 
camera.release()
cv2.destroyAllWindows()
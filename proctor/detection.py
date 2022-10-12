import cv2
import numpy as np
import math
from face_detector import get_face_detector, find_faces
from face_landmarks import get_landmark_model, detect_marks
import numpy as np
import cv2
import joblib
from face_detector import get_face_detector, find_faces
from head_pose import *
from encode import Encode
from recognition import Recognition
import json
import time
import datetime
import pandas as pd
import csv


start_time = time.time()
total_time = 20
working_time = 0
img_path = r'C:\Users\SURYA S\proctor\main\Images'
enc = Encode(img_path)
enc.names()
enc.findEncodings()
enc.save()
with open('model.json') as f:
    data = json.load(f)
         
eList = []
cNames = data['classNames']
for i in range(len(cNames)):
    eList.append(np.array(data['encodeList'][i]))
             
        
rec = Recognition(eList, cNames)

def markAttendance(id, name, working_time):
    rtime = total_time - working_time
    ntotal_time = str(datetime.timedelta(seconds=total_time))
    nworking_time = str(datetime.timedelta(seconds=working_time))
    nrtime = str(datetime.timedelta(seconds=rtime))
    with open(r'report.csv', 'a', newline='') as csvfile:
        fieldnames = ['Id','Name', 'TotalWtime', 'EfficientWtime', 'Rtime']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({'Id':id, 'Name':name, 'TotalWtime':ntotal_time, 'EfficientWtime':nworking_time, 'Rtime':nrtime})




#head_pose
face_model = get_face_detector()
landmark_model = get_landmark_model()
cap = cv2.VideoCapture(0)
ret, img = cap.read()
size = img.shape
font = cv2.FONT_HERSHEY_SIMPLEX 
# 3D model points.
model_points = np.array([
                            (0.0, 0.0, 0.0),             # Nose tip
                            (0.0, -330.0, -65.0),        # Chin
                            (-225.0, 170.0, -135.0),     # Left eye left corner
                            (225.0, 170.0, -135.0),      # Right eye right corne
                            (-150.0, -150.0, -125.0),    # Left Mouth corner
                            (150.0, -150.0, -125.0)      # Right mouth corner
                        ])

# Camera internals
focal_length = size[1]
center = (size[1]/2, size[0]/2)
camera_matrix = np.array(
                         [[focal_length, 0, center[0]],
                         [0, focal_length, center[1]],
                         [0, 0, 1]], dtype = "double"
                         )

cap2 = cv2.VideoCapture(0)
while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    if elapsed_time>total_time:
        print("Time Limit Reached!!")
        id = int(input("Enter Id: "))
        name = input("Enter the Name: ")
        
        markAttendance(id, name, working_time)
        print("Program Exiting.....")
        break
    
    ret, img = cap2.read()
    if not ret:
        print("Can't capture")
        break
    faces = find_faces(img, face_model)
    
    #face spoofing
    result = rec.recog(img)
    #name, x1, x2, y1, y2 = result
    #if name=="Unknown":
        #print("Unknown Face Detected")
        #continue
    #head pose            
    for face in faces:
        marks = detect_marks(img, landmark_model, face)
        # mark_detector.draw_marks(img, marks, color=(0, 255, 0))
        image_points = np.array([
                                marks[30],     # Nose tip
                                marks[8],     # Chin
                                marks[36],     # Left eye left corner
                                marks[45],     # Right eye right corne
                                marks[48],     # Left Mouth corner
                                marks[54]      # Right mouth corner
                            ], dtype="double")
        dist_coeffs = np.zeros((4,1)) # Assuming no lens distortion
        (success, rotation_vector, translation_vector) = cv2.solvePnP(model_points, image_points, camera_matrix, dist_coeffs, flags=cv2.SOLVEPNP_UPNP)
        
        
        # Project a 3D point (0, 0, 1000.0) onto the image plane.
        # We use this to draw a line sticking out of the nose
        
        (nose_end_point2D, jacobian) = cv2.projectPoints(np.array([(0.0, 0.0, 1000.0)]), rotation_vector, translation_vector, camera_matrix, dist_coeffs)
        
        for p in image_points:
            cv2.circle(img, (int(p[0]), int(p[1])), 3, (0,0,255), -1)
        
        
        p1 = ( int(image_points[0][0]), int(image_points[0][1]))
        p2 = ( int(nose_end_point2D[0][0][0]), int(nose_end_point2D[0][0][1]))
        x1, x2 = head_pose_points(img=img, rotation_vector=rotation_vector, translation_vector=translation_vector, camera_matrix=camera_matrix)

        #cv2.line(img, p1, p2, (0, 255, 255), 2)
        #cv2.line(img, tuple(x1), tuple(x2), (255, 255, 0), 2)
        # for (x, y) in marks:
        #     cv2.circle(img, (x, y), 4, (255, 255, 0), -1)
        # cv2.putText(img, str(p1), p1, font, 1, (0, 255, 255), 1)
        try:
            m = (p2[1] - p1[1])/(p2[0] - p1[0])
            ang1 = int(math.degrees(math.atan(m)))
        except:
            ang1 = 90
            
        try:
            m = (x2[1] - x1[1])/(x2[0] - x1[0])
            ang2 = int(math.degrees(math.atan(-1/m)))
        except:
            ang2 = 90
            
            # print('div by zero error')
            
        if ang1<48 and ang1>-48 and ang2<48 and ang2>-48 and result:
            working_time += time.time()-current_time
            
        if ang1 >= 48:
            #print('Head down')
            cv2.putText(img, 'Head down', (30, 30), font, 2, (255, 255, 128), 3)
        elif ang1 <= -48:
            #print('Head up')
            cv2.putText(img, 'Head up', (30, 30), font, 2, (255, 255, 128), 3)
            
        if ang2 >= 48:
            #print('Head right')
            cv2.putText(img, 'Head right', (90, 30), font, 2, (255, 255, 128), 3)
        elif ang2 <= -48:
            #print('Head left')
            cv2.putText(img, 'Head left', (90, 30), font, 2, (255, 255, 128), 3)
        
        cv2.putText(img, str(ang1), tuple(p1), font, 2, (128, 255, 255), 3)
        cv2.putText(img, str(ang2), tuple(x1), font, 2, (255, 255, 128), 3)
        #cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
        #cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
        #cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
    cv2.imshow('img', img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
cv2.destroyAllWindows()
cap.release()


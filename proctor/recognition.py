import cv2
import numpy as np
import face_recognition.api as face_recognition
import os


class Recognition:
    def __init__(self, encodeList, classNames):
        self.encodeListKnown = encodeList
        self.classNames = classNames
        
    def recog(self, img):
        face_recognition.tolerance = 0.55
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
        
        for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
            matches = face_recognition.compare_faces(self.encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(self.encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = self.classNames[matchIndex].upper()
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
                cv2.rectangle(img, (x1,y2-35), (x2,y2), (0,255,0), cv2.FILLED)
                cv2.putText(img,name, (x1+6,y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
                #return name, x1, x2, y1, y2
                return 1
            else:
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
                cv2.rectangle(img, (x1,y2-35), (x2,y2), (0,255,0), cv2.FILLED)
                cv2.putText(img,"Unknown", (x1+6,y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
                #return name, x1, x2, y1, y2
                return 0

        
    
    

 
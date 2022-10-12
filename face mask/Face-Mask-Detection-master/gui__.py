import tkinter as tk
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import numpy as np
import imutils
import time
import cv2
import os
frequency=2500
duration=50
import glob
import matplotlib.pyplot as plt 
from tkinter import filedialog
from tkinter import *
from PIL import  Image
from keras import models  
from tensorflow.keras import preprocessing, layers, models, callbacks 
import cv2
from tensorflow.keras.models import load_model
from keras import models 
global loadedModel
import numpy

import imutils
import numpy as np
import glob
import imutils
import numpy as np
from keras import models  
from tensorflow.keras import preprocessing, layers, models, callbacks 
from sklearn.metrics import pairwise
import time
import os  # Operating system functionality
import random  # Random number generator
import pandas as pd  # Data analysis & manipulation
import numpy as np  # Array-processing
import seaborn as sns  # Data visualization
import matplotlib.pyplot as plt  # Data visualization
from tensorflow.keras import preprocessing, layers, models, callbacks  # Neural networks
from sklearn import metrics  # Model evaluation
global loadedModel
size = 30
from PIL import Image, ImageTk
from tkinter import *

import numpy as np
import cv2
from keras.preprocessing import image
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
#from keras import models
from tensorflow.keras.models import load_model
# loading Python Imaging Library 
from PIL import ImageTk, Image   
# To get the dialog box to open when required  
from tkinter import filedialog 




                 
#initialise GUI
top=tk.Tk()
top.geometry('800x600')
top.title('Detector')
top.configure(background='#CDCDCD')

label=Label(top,background='#CDCDCD', font=('arial',15,'bold'))



   

 



def yes():
    
    
    
    # load our serialized face detector model from disk
    prototxtPath = 'face_detector/deploy.prototxt'
    weightsPath =  'face_detector/res10_300x300_ssd_iter_140000.caffemodel'
    faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

# load the face mask detector model from disk
    maskNet = load_model("mask_detector.model")

# initialize the video stream
    print("[INFO] starting video stream...")
    camera = cv2.VideoCapture(0)

# loop over the frames from the video stream
    while True:
        (_,frame) = camera.read()
        frame = imutils.resize(frame, width=400)
        (locs, preds) = detect_and_predict_mask(frame, faceNet, maskNet)
        for (box, pred) in zip(locs, preds):
                
            (startX, startY, endX, endY) = box
            (mask, withoutMask) = pred
            label = "Mask" if mask > withoutMask else "No Mask"
            color = (0, 255, 0) if label == "Mask" else (0, 0, 255)
            if label!="Mask":
                #winsound.Beep(frequency,duration)
                label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)
                cv2.putText(frame, label, (startX, startY - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
                cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
    cv2.destroyAllWindows()
    vs.stop()
        


def detect_and_predict_mask(frame, faceNet, maskNet):
	(h, w) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(frame, 1.0, (224, 224),
		(104.0, 177.0, 123.0))
	faceNet.setInput(blob)
	detections = faceNet.forward()
	faces = []
	locs = []
	preds = []

	# loop over the detections
	for i in range(0, detections.shape[2]):
		confidence = detections[0, 0, i, 2]
		if confidence > 0.5:
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")
			(startX, startY) = (max(0, startX), max(0, startY))
			(endX, endY) = (min(w - 1, endX), min(h - 1, endY))
			face = frame[startY:endY, startX:endX]
			face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
			face = cv2.resize(face, (224, 224))
			face = img_to_array(face)
			face = preprocess_input(face)
			faces.append(face)
			locs.append((startX, startY, endX, endY))
	if len(faces) > 0:
		faces = np.array(faces, dtype="float32")
		preds = maskNet.predict(faces, batch_size=32)
	return (locs, preds)









   
btn_real = Button(top, text ='REAL_TIME', bg='#0052cc', fg='#ffffff',width=10, height=2,command = yes).place( 
                                        x = 500, y= 200) 
btn_exit = Button(top, text ='EXIT', bg='#0052cc', fg='#ffffff',width=10, height=2,command = top.destroy).place( 
                                        x = 200, y= 200)


label.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Mask Detector",pady=20, font=('arial',30,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()
top.mainloop()

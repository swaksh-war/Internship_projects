import os
import cv2

PATH_TO_OLD_IMAGES = r"/home/dingo/code/internship_projects/Internship_projects/instagram_influencer_image_classification/data"
PATH_TO_SAVE = r"/home/dingo/code/internship_projects/Internship_projects/instagram_influencer_image_classification/resnetdata"
for folder in os.listdir(PATH_TO_OLD_IMAGES):
    for image in os.listdir(PATH_TO_OLD_IMAGES + '/' + str(folder)):
        img = cv2.imread(PATH_TO_OLD_IMAGES + '/' + str(folder) + '/' + str(image), cv2.IMREAD_COLOR)
        resized_img = cv2.resize(img,(32,32))
        cv2.imwrite(PATH_TO_SAVE + '/' + str(folder) + '/' + str(image), resized_img)
        

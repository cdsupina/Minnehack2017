import cv2
import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3
import time
import os
from auth import *
import pyimgur
from img_locs import *

#initialize imgur api
im = pyimgur.Imgur(im_client_id)

vis_rec = VisualRecognitionV3('2016-05-20', api_key=watson_auth)

#make directories for storing videos and frames if not created already
game_num = 0

subject_name = input('Enter the name of the subject: ')

#make folder for session
if not os.path.exists(subject_name):
    os.makedirs(subject_name)



cap = cv2.VideoCapture(1)

img_idx = 0


while True:
    ret,frame = cap.read()
    cv2.imshow('frame',frame)

    k = cv2.waitKey(1)&0xFF
    if k == ord('q'):
        break
    elif k == ord('c'):
        path = subject_name + '/' + str(time.time()) + '.png'
        cv2.imwrite(path, frame)
      #  uploaded_img = im.upload_image(path, title = str(img_idx) + '.png')
     #   img_link = uploaded_img.link
#        response = vis_rec.classify(images_url=img_link)
 #       classes = response['images'][0]['classifiers'][0]['classes']
    #    print(img_link)
  #      for c in classes:
   #         print(c)
        img_idx += 1

cap.release()
cv2.destroyAllWindows()

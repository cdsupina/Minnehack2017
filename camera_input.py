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

#make folder for session
while(os.path.exists('session_' + str(game_num))):
    game_num += 1

game_id = 'session_' + str(game_num)

os.makedirs(game_id)

cap = cv2.VideoCapture(1)

img_idx = 0


while True:
    ret,frame = cap.read()
    cv2.imshow('frame',frame)

    k = cv2.waitKey(1)&0xFF
    if k == ord('q'):
        break
    elif k == ord('c'):
        path = game_id + '/' + str(img_idx) + '.png'
        cv2.imwrite(path, frame)
        uploaded_img = im.upload_image(path, title = str(img_idx) + '.png')
        img_link = uploaded_img.link
        response = vis_rec.classify(images_url=img_link)
        classes = response['images'][0]['classifiers'][0]['classes']
        print(img_link)
        for c in classes:
            print(c)
        img_idx += 1

cap.release()
cv2.destroyAllWindows()

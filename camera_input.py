import cv2
import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3
import time
import os
from auth import *
import pyimgur
import sys
from twilio.rest import TwilioRestClient

cal_count = 0

#initialize imgur api
im = pyimgur.Imgur(im_client_id)

vis_rec = VisualRecognitionV3('2016-05-20', api_key=watson_auth)
twilio_client = TwilioRestClient(twilio_account_sid, twilio_auth_token)

#make directories for storing videos and frames if not created already
session_num = 0

#make folder for session

if not os.path.exists('sessions'):
    os.makedirs('sessions')
while(os.path.exists('sessions/session_' + str(session_num))):
    session_num += 1

session_id = 'sessions/session_' + str(session_num)

os.makedirs(session_id)

cap = cv2.VideoCapture(1)

img_idx = 0

cal_dict={'soda': 140,'pretzels': 300,'granolabars': 190,'pizza': 300,'soylent': 400}

send_count = 1000
links = []
while True:
    ret,frame = cap.read()
    cv2.imshow('frame',frame)

    k = cv2.waitKey(1)&0xFF
    if k == ord('q'):
        break
    elif k == ord('c'):
        path = session_id + '/' + str(img_idx) + '.png'
        cv2.imwrite(path, frame)
        uploaded_img = im.upload_image(path, title = str(img_idx) + '.png')
        img_link = uploaded_img.link
        response = vis_rec.classify(images_url=img_link, classifier_ids = ['foods_pizza_1319063426','foods_pretzel_125371200','foods_soda_828646275','foods_soylent_177286879','foods_granolabars_1605587790'])
        classes = response['images'][0]['classifiers'][0]['classes']
        print(img_link)
        links.append(img_link)
       # print(response)
        if len(classes) >= 1:
            for c in classes:
                print(c['class'] + ' ' + str(c['score']) + ' ' + str(cal_dict[c['class']]) + ' calories')
                cal_count += cal_dict[c['class']]
                print('Total Calories: ' + str(cal_count))
                if cal_count >= send_count:
                    twilio_client.messages.create(to='+14088934962',from_='+14083421269',body='You have consumed ' + str(cal_count) + ' calories! ' + str(links))
                    send_count+=1000
                    links = []
            img_idx += 1

cap.release()
cv2.destroyAllWindows()

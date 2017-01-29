import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3
from PIL import Image


visual_recognition = VisualRecognitionV3('2016-05-20', api_key="436d32ce5fe192a099dd78e85d6895efd9ae0642")

#image = open('session_2/0.png', encoding='utf-8')
response = visual_recognition.classify(images_url='https://scontent-ort2-1.xx.fbcdn.net/v/t34.0-12/16425628_10154502584839032_993101943_n.png?oh=f6e3a8cf2e9b40ad1d2ae15f02d1cb13&oe=58905869')
#classify via file

classes = response['images'][0]['classifiers'][0]['classes']

for i in classes:
    print(i)

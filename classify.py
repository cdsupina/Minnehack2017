import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3('2016-05-20', api_key="436d32ce5fe192a099dd78e85d6895efd9ae0642")

response = visual_recognition.classify(images_url='https://www.ibm.com/ibm/ginni/images/ginni_bio_780x981_v4_03162016.jpg')

classes = response['images'][0]['classifiers'][0]['classes']

for i in classes:
    print(i)

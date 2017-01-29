import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3
import time
import os
from auth import *
import pyimgur

vr = VisualRecognitionV3('2016-05-20',api_key=watson_auth)


print(vr.list_classifiers())


with open(join(dirname('__file__'), 'pretzels.zip'), 'rb') as pretzels,open(join(dirname('__file__'),'not_pretzels.zip'), 'rb') as notpretzels,open(join(dirname('__file__'),'granola_bars.zip'), 'rb') as granolabars,open(join(dirname('__file__'),'not_granola_bars.zip'), 'rb') as notgranolabars,open(join(dirname('__file__'),'pizza.zip'), 'rb') as pizza,open(join(dirname('__file__'),'not_pizza.zip'), 'rb') as notpizza,open(join(dirname('__file__'),'soda.zip'),'rb') as soda,open(join(dirname('__file__'),'not_soda.zip'),'rb') as notsoda,open(join(dirname('__file__'), 'soylent.zip'), 'rb') as soylent,open(join(dirname('__file__'),'not_soylent.zip'),'rb') as notsoylent:
 #   vr.create_classifier('foods_pretzel', pretzels_positive_examples=pretzels, negative_examples=notpretzels)
 #   vr.create_classifier('foods_granolabars', granolabars_positive_examples=granolabars, negative_examples=notgranolabars)
 #   vr.create_classifier('foods_pizza', pizza_positive_examples=pizza, negative_examples=notpizza)
 #   vr.create_classifier('foods_soda', soda_positive_examples=soda, negative_examples=notsoda)
    vr.delete_classifier('foods_280466332')
    vr.create_classifier('foods_soylent', soylent_positive_examples=soylent, negative_examples=notsoylent)

print(vr.list_classifiers())

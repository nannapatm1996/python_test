# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 16:17:30 2020

@author: user
"""
import multiprocessing
import threading
#_multiprocessing.sem_unlink = None
import numpy as np
import tensorflow as tf
#from flask import Flask,jsonify
from tensorflow.keras.preprocessing import image
from os.path import dirname, join
from PIL import Image



""" Load the pretrained model """
#with open('PrayingTL_model.json', 'r')as f:
#    model_json = f.read()
#model = tf.keras.models.model_from_json(model_json) #Loading model structure
#model.load_weights('PrayingTL_model.h5') #Loading model weights

def threading_func(name):
    def f(self, *args, **kwargs):
        return getattr(threading, name)(*args, **kwargs)
    f.__name__ = f.__qualname__ = name
    return f

ctx = multiprocessing.get_context()
for name in ["Lock", "RLock", "Condition", "Semaphore", "BoundedSemaphore",
             "Event", "Barrier"]:
    setattr(type(ctx), name, threading_func(name))
    setattr(multiprocessing, name, getattr(ctx, name))

def classify_image(img_name):
    #upload_dir = 'uploads/'
    #json_file = join(dirname(pre.__file__),'PrayingTL_model.json')
    #print(json_file)

    with open(join(dirname(__file__),'PrayingTL_model.json'), 'r') as f:
        model_json = f.read()
    model = tf.keras.models.model_from_json(model_json) #Loading model structure
    model.load_weights(join(dirname(__file__),'PrayingTL_model.h5')) #Loading model weights
    image_path = join(dirname(__file__),img_name)
    #img = image.load_img(image_path, target_size=(128,128))
    #img = tf.keras.preprocessing.image.load_img(image_path, target_size=(128,128))
    img = Image.open(image_path)
    img = img.resize((128,128))
    #x = image.img_to_array(img)
    x = tf.keras.preprocessing.image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    prediction= model.predict(x)
    print('Image_path:{}'.format(image_path))
    print('Prediction Value:{}'.format(prediction[0][0]))
    
    if prediction[0] >= 0.0001:
        print('Prediction Result: Sitting')
        return 'Prediction Result: Sitting'
        #return jsonify({"object_detected:":"sitting","value":str(prediction[0][0])})
    else:
        print('Prediction Result: Prostrating')
        return 'Prediction Result: Prostrating'
        #return jsonify({"object_detected:":"prostrating","value":str(prediction[0][0])})
        


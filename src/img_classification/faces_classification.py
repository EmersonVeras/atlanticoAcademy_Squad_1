# -*- coding: utf-8 -*-
"""Face recogonition.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fty9mphvDZ_8WRteiqmF0EPZITXsmFFa

Requisitos do projeto:
- É necessário identificar uma face
- É necessário utilizar 3 técnicas de pré-processamento
- É necessário utilizar uma rede neural pré-treinada
- É necessário criar uma rede neural
- É necessário criar um relatório comparando o desempenho
- É necessário realizar o cálculo de métricas de desempenho
- É necessário realizar a apresentação das estratégias
"""

from PIL import Image
import cv2
import numpy as np
#from google.colab.patches import cv2_imshow
from cv2 import imshow
#from google.colab import drive
import os
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

import random
import tensorflow as tf
import cv2 as cv
import os 
import glob

import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Nadam, Adam
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Dropout, Flatten, Input, Dense
from tensorflow.keras.layers import Conv2D, MaxPooling2D, BatchNormalization

import tensorflow
from tensorflow.keras import applications
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split


# Reading the dataset and creating the labels for input data
def create_input_labels():
  base_dir = '../../data/faces-classification/'
  felipe_dir = glob.glob(os.path.join(base_dir + 'felipe/', '*'))
  emerson_dir = glob.glob(os.path.join(base_dir + 'emerson/', '*'))
  luan_dir = glob.glob(os.path.join(base_dir + 'luan/', '*'))
  X_path = felipe_dir + emerson_dir + luan_dir
  print("\nTotal # of inputs: {}".format(len(X_path)))
  X = []
  for f in X_path:
    X.append(np.array(cv.resize(cv.imread(f), (224,224), interpolation = cv.INTER_AREA)))     
  X = np.array(X)
  X = X / 255

  l_felipe = np.zeros(len(felipe_dir))
  l_felipe_string = ['felipe' for i in range(len(felipe_dir))]
  
  l_emerson = np.ones(len(emerson_dir))
  l_emerson_string = ['emerson' for i in range(len(emerson_dir))]
  
  l_luan = 2*np.ones(len(luan_dir))
  l_luan_string = ['rose' for i in range(len(luan_dir))]
  
  y_string = np.concatenate((l_felipe_string, l_emerson_string, l_luan_string))
  y = np.concatenate((l_felipe, l_emerson, l_luan))
  y = to_categorical(y, 3)

  return X, y

def create_model():
  # load a pretrained network
  vgg = tensorflow.keras.applications.VGG16(input_shape=(224,224,3), include_top = False, weights= 'imagenet')
  print(vgg.summary())
  x = vgg.output
  x = Flatten()(x)
  x = Dense(3078,activation='relu')(x) 
  x = Dropout(0.5)(x)
  x = Dense(256,activation='relu')(x) 
  x = Dropout(0.2)(x)

  # 3 is the number of classes. May change as we add more images
  out = Dense(3,activation='softmax')(x) 

  tf_model = Model(inputs=vgg.input,outputs=out)
  for layer in tf_model.layers[:20]:
    layer.trainable=False
  return tf_model


def train_model(model, X_train, X_val, y_train, y_val):
  filepath = 'TF-CNN.{epoch:02d}-{loss:.2f}-{accuracy:.2f}-{val_loss:.2f}-{val_accuracy:.2f}.hdf5'
  lr_red = keras.callbacks.ReduceLROnPlateau(monitor='acc', patience=3, verbose=1, factor=0.5, min_lr=0.000001)
  chkpoint = keras.callbacks.ModelCheckpoint(filepath, monitor='val_acc', verbose=0, save_best_only=True, save_weights_only=False, mode='auto', period=1)
  model.compile(optimizer = Nadam(0.0001) , loss = 'categorical_crossentropy', metrics=["accuracy"])

  history = model.fit(X_train, y_train, batch_size = 1, epochs = 30, initial_epoch = 0, 
    validation_data = (X_val, y_val), callbacks=[lr_red, chkpoint])


def main():
  # read data and create labels
  X, y = create_input_labels()

  # split train and test sets
  X_train, X_val, y_train, y_val = train_test_split(X, y, test_size = 0.2, random_state=42)
  X = []

  model = create_model()
  model.summary()

  train_model(model, X_train, X_val, y_train, y_val)


if __name__ == "__main__": 
  main()
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

# Imports from third parties


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

import keras
from keras import metrics
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

# Imports from our own files
from file_utils import list_all_inputs
from preprocessing import histogram_equalization
from metrics import sensitivity, specificity


# Reading the dataset and creating the labels for input data
def create_input_labels(hist_equalization=False):  
  X_path, labels = list_all_inputs()
  print("\nTotal # of inputs: {}".format(len(X_path)))
  print("Labels: {}".format(labels))
  if hist_equalization:
    print("Applying histogram equalization")
  X = []
  y = []
  for i, (folder, label) in enumerate(zip(X_path, labels)):
    for f in folder:
      img = np.array(cv.resize(cv.imread(f), (224,224), interpolation = cv.INTER_AREA))
      if(hist_equalization):
        img = histogram_equalization(img)
      X.append(img)     
      y.append(i)

  X = np.array(X)
  X = X / 255

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


def train_model(model, id, X_train, X_val, y_train, y_val):
  filepath = id + '_TF-CNN.{epoch:02d}-{loss:.2f}-{accuracy:.2f}-{val_loss:.2f}-{val_accuracy:.2f}.hdf5'
  lr_red = keras.callbacks.ReduceLROnPlateau(monitor='accuracy', 
    patience=3, verbose=1, factor=0.5, min_lr=0.000001)
  chkpoint = keras.callbacks.ModelCheckpoint(filepath, 
    monitor='val_accuracy', verbose=0, save_best_only=True, 
    save_weights_only=False, mode='auto', period=1)
  
  history_filename = 'log_' + id + '.csv'
  history_cb = tf.keras.callbacks.CSVLogger(history_filename, separator=",", append=False)

  model_metrics=['accuracy', 
                  tf.keras.metrics.Precision(),                  
                  tf.keras.metrics.Recall(),
                  sensitivity,
                  specificity]
  model.compile(optimizer = Nadam(0.0001) , loss = 'categorical_crossentropy', 
    metrics=model_metrics)

  history = model.fit(X_train, y_train, batch_size = 1, epochs = 30, initial_epoch = 0, 
    validation_data = (X_val, y_val), callbacks=[lr_red, chkpoint, history_cb])


def main():
  # read data and create labels
  X, y = create_input_labels(hist_equalization=True)

  # split train and test sets
  X_train, X_val, y_train, y_val = train_test_split(X, y, test_size = 0.2, random_state=42)
  X = []

  model = create_model()
  model.summary()
  
  train_model(model, "histogram_equalization", X_train, X_val, y_train, y_val)


if __name__ == "__main__": 
  main()

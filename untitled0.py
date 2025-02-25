# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/160OtwtKKDXwjwmmcnnnSI-IkvrXcCeng

# **Hand Written Digit prediction_classificartion Analysis**

The digits dataset consist of 8x8 pixel images attributes of the dataset stores 8x8 array of grayscale value for each image. we wil use these arrays to visualise the first 4 images .The target attribute of the dataset stores the digit each image represent
"""



"""# Import library"""



"""This is a data (dummy) of financial market top 25 news for the"""



import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

"""# import csv as dataframe"""

from sklearn.datasets import load_digits

df = load_digits()

_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10,3))
for ax, image, label in zip(axes, df.images, df.target):
  ax.set_axis_off()
  ax.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
  ax.set_title("Training: %i" % label)

"""# shape of data"""

df.images.shape

df.images[0]

df.images[0].shape

len(df.images)

n_samples = len(df.images)
data = df.images.reshape(n_samples, -1)

data[0].shape

data.shape

"""# Scaling image data"""

data.min()

data.max()

data = data/16

data.min()

data.max()

data[0]

"""# Train Test Split data"""

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test =train_test_split(data, df.target, test_size=0.3)

x_train.shape, x_test.shape, y_train.shape, y_test.shape
((1257,64), (540,64), (1257,), (540,))

"""# Random forest model"""

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier()

rf.fit(x_train, y_train)

"""# predict test data"""

y_pred = rf.predict(x_test)

y_pred

"""# model accurecy"""

from sklearn.metrics import confusion_matrix, classification_report

confusion_matrix(y_test,y_pred)

print(classification_report(y_test, y_pred))
import tensorflow as tf
import numpy as np
import random
import math
import matplotlib.pyplot as plt

DataSet=np.genfromtxt("DataSet.csv", delimiter=",")
Input = DataSet[:,0:2]
Output =  DataSet[:,2]


model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(10, activation='relu'),
  tf.keras.layers.Dense(1000, activation='linear'),
  tf.keras.layers.Dense(1000, activation='linear'),
  tf.keras.layers.Dense(100, activation='linear'),
  tf.keras.layers.Dense(1, activation='linear')
])

model.compile(optimizer='adam', loss='mean_absolute_error', metrics=['accuracy'])
print(len(Output))
model.fit(Input, Output, epochs=25)

model.save('GunNet')
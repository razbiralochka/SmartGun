import tensorflow as tf
import numpy as np
import random
import math
import matplotlib.pyplot as plt

DataSet=np.genfromtxt("DataSet.csv", delimiter=",")

print(DataSet)
Input = DataSet[:,0:2]
Output = DataSet[:,2]
print(Input)

model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(50, activation='linear',input_dim=2),
  tf.keras.layers.Dense(300, activation='elu'),
  tf.keras.layers.Dense(500, activation='elu'),
  tf.keras.layers.Dropout(0.1),
  tf.keras.layers.Dense(20, activation='relu'),
  tf.keras.layers.Dense(1)
])

model.compile(optimizer=tf.keras.optimizers.RMSprop(lr=0.0001), loss='mse', metrics=['acc'])
print(len(Output))
model.fit(Input, Output, epochs=5000)
plt.plot(Input,Output)
outputT=model.predict(Input)

print(outputT)
plt.plot(Input,outputT)

plt.show()
model.save('GunNet')
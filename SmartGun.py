import tensorflow as tf
import numpy as np
import random
import math
import matplotlib.pyplot as plt



GunNet = tf.keras.models.load_model('GunNet')

Velocity = 150
Lenght = 200

Target = [[Velocity,Lenght]]

AngleTensor = GunNet.predict(Target)


Angle=AngleTensor[0,0]


#Angle=15

print(Angle)

y=0
x=0
Vx=Velocity*math.cos(math.pi*Angle/180)
Vy=Velocity*math.sin(math.pi*Angle/180)
while y>=0:
   Vx=Vx-(1.2258/2*pow(Vx,2)*0.02)*0.01
   Vy=Vy-(1.2258/2*pow(Vy,2)*0.02+9.81)*0.01
   x=x+Vx*0.1
   y=y+Vy*0.1
print(x)
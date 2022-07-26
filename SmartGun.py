import tensorflow as tf
import numpy as np
import random
import math
import matplotlib.pyplot as plt
GunNet = tf.keras.models.load_model('GunNet')

L=input("Distanse to Target: ")
L=float(L)
Target = [[L]]

AngleTensor = GunNet.predict(Target)
Angle=AngleTensor[0,0]
X=[]
Y=[]
y=0
x=0
Vx=200*math.cos(math.pi*Angle/180)
Vy=200*math.sin(math.pi*Angle/180)
while y>=0:
    X.append(x)
    Y.append(y)
    Vx=Vx-(1.2258*pow(Vx,2)/2*0.0005)*0.01
    Vy=Vy-(1.2258*(Vy*abs(Vy))/2*0.0005+9.81)*0.01
    x=x+Vx*0.01
    y=y+Vy*0.01
plt.plot(X,Y)
plt.axis('equal')
print('Angle: ',Angle)
print('x: ',x)
print('Delta',(x-L))  

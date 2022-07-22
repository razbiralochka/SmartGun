#from keras.models import Sequential
#from keras.layers import Dense
import numpy as np
import random
import math
import matplotlib.pyplot as plt

DataSet=np.zeros((10000,3))

for i in range(10000):
    DataSet[i,0] = random.randint(100, 250)
    DataSet[i,2] = random.randint(5, 450)/10
print(DataSet)

Velocity=DataSet[:,0]
Angle=DataSet[:,2]



for i in range(len(Velocity)):
    y=0
    x=0
    Vx=Velocity[i]*math.cos(math.pi*Angle[i]/180)
    Vy=Velocity[i]*math.sin(math.pi*Angle[i]/180)
    while y>=0:
       Vx=Vx-(1.2258/2*pow(Vx,2)*0.02)*0.01
       Vy=Vy-(1.2258/2*pow(Vy,2)*0.02+9.81)*0.01
       x=x+Vx*0.1
       y=y+Vy*0.1
       DataSet[i,1]=x
print(DataSet)
Lenght=DataSet[:,1]

plt.plot(Lenght)

np.savetxt("DataSet.csv", DataSet, delimiter=",")
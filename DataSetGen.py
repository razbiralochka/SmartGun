#from keras.models import Sequential
#from keras.layers import Dense
import numpy as np
import random
import math
import matplotlib.pyplot as plt

DataSet=np.zeros((1000,3))

for i in range(1000):
    DataSet[i,2] = random.randint(0,45)
    DataSet[i,1] = random.randint(50,200)
Angle=DataSet[:,2]
Vel=DataSet[:,1]
for i in range(len(Angle)):
    y=0
    x=0
    Vx=Vel[i]*math.cos(math.pi*Angle[i]/180)
    Vy=Vel[i]*math.sin(math.pi*Angle[i]/180)
    while y>=0:
       Vx=Vx-(1.2258*pow(Vx,2)/2*0.0005)*0.01
       Vy=Vy-(1.2258*(Vy*abs(Vy))/2*0.0005+9.81)*0.01
       x=x+Vx*0.01
       y=y+Vy*0.01
       DataSet[i,0]=x
print(Angle)
Lenght=DataSet[:,0]

plt.plot(Angle,Lenght)

print(DataSet)
np.savetxt("DataSet.csv", DataSet, delimiter=",")
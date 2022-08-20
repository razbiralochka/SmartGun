import math

def shoot(angle):
    vel=200
    y=0
    x=0
    Vx=vel*math.cos(math.pi*angle/180)
    Vy=vel*math.sin(math.pi*angle/180)
    while y>=0:
       Vx=Vx-(1.2258*pow(Vx,2)/2*0.0005)*0.01
       Vy=Vy-(1.2258*(Vy*abs(Vy))/2*0.0005+9.81)*0.01
       x=x+Vx*0.01
       y=y+Vy*0.01
    return x
   
    
a=shoot(20)

print(a)

a=shoot(30)

print(a)
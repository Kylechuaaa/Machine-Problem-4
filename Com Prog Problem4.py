import math as mt
import numpy as np
import matplotlib.pyplot as plt
import sys

print('')
print('Enter values angle, acceleration in x axis and y axis, velocity and height')

phi = float(input('Angle the initial height emerged: '))
accelerationhorizontal = float(input('Body acceleration in the x-axis: '))
accelerationvertical = float(input('Body acceleration in the y-axis: '))
velocity = float(input('The initial velocity of the body: '))
height = float(input('The height applies to the surface: '))

if accelerationvertical == 0:
    sys.exit(':0 Do not input zero value body acceleration value in the y-axis acceleration :) ')

    
gap = mt.sqrt(velocity**2 - height*4*(1/2*accelerationvertical))
tude = mt.radians(phi)  
velocityY = mt.sin(tude)*velocity
velocityX = mt.cos(tude)*velocity 
time = (gap - velocityY) / accelerationvertical
time1 = (-gap - velocityY ) / accelerationvertical
             
        
if time <= 0:    
    time = time1                          
    horizontal = 0.5*np.linspace(0,time)**2*accelerationhorizontal + (np.linspace(0,time))*velocityX 
    vertical =  0.5*np.linspace(0,time)**2*accelerationvertical + (np.linspace(0,time))*velocityY
    
else:
    horizontal = 0.5*np.linspace(0,time)**2*accelerationhorizontal + (np.linspace(0,time))*velocityX
    vertical = 0.5*np.linspace(0,time)**2*accelerationvertical + np.linspace(0,time)*velocityY
        
    
plt.plot(horizontal,vertical)
plt.ylabel('Y direction')                        
plt.xlabel('X direction')
plt.grid()
plt.suptitle('Trajectory Plot')
plt.show()

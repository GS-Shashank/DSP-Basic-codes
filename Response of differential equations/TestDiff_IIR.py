"""

#######################################
    IIR system
    
    code by: GSS
#######################################
Consider the equation
     
y(n)=0.2x(n)+0.4x(n-1)+0.5y(n-2)

Let us solve the difference equation for the IIR system

chose x(n)= delta function and find h(n)
chose x(n)= step function and find y(n)

"""
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

#co-efficients of the differential equation

B=[0.2 ,0.4]
A=[1 ,-0.5]

n=np.arange(0,10,1)

#calculating Impulse response
x=signal.unit_impulse(10)
h=signal.lfilter(B,A,x)

#Plotting Impulse response

plt.stem(n,h,use_line_collection=True,markerfmt="o")
plt.title("Impulse Response")
plt.xlabel("n")
plt.ylabel("h(n)")
plt.axhline(color="red", zorder=-1)
plt.axvline(color="red", zorder=-1)
plt.grid(1)
plt.show()

#calculating Step response
x=np.ones(10)
y=signal.lfilter(B,A,x)

#plotting step response
plt.stem(n,y,use_line_collection=True,markerfmt="o")
plt.title("Step Response")
plt.xlabel("n")
plt.ylabel("y(n)")
plt.axhline(color="red", zorder=-1)
plt.axvline(color="red", zorder=-1)
plt.grid(1)
plt.show()

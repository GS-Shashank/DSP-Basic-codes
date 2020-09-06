"""
    fft 2
    
    code by: GSS

"""


import numpy as np
import matplotlib.pyplot as plt

def plotter(a,b):
    plt.axhline(color="gray", zorder=-1)
    plt.axvline(color="gray", zorder=-1)
    plt.grid(1)
    plt.plot(a,b)
    plt.show()
   
t=np.arange(-2,2.1,0.1)
y1=np.zeros(int(len(t)/4))
y2=np.ones(int(len(t)/2))
y3=np.zeros((int(len(t)/4)+1))
y=np.concatenate((y1,y2,y3))
plotter(t,y)

z=np.zeros(512-len(y))
y=np.concatenate((y,z))
n=len(y)
Y=abs(np.fft.fft(y))
f=np.arange(-n/2,(n/2))
z=np.fft.fftshift(Y)
plotter(f,z)
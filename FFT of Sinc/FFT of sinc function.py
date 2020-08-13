

"""
    FFT 
    
    Code by :- GSS
"""


import numpy as np
import matplotlib.pyplot as plt

def plotter(a,b):
    plt.axhline(color="gray", zorder=-1)
    plt.axvline(color="gray", zorder=-1)
    plt.grid(1)
    plt.plot(a,b)
    plt.show()
   
# to plot Sinc wave
t=np.linspace(-5,5,50)
y=np.sinc(t)
plotter(t,y)


# to plot the sampled wave
z=np.zeros(512-len(y))
y=np.concatenate((y,z))
n=len(y)
Y=abs(np.fft.fft(y))
f=np.arange(-n/2,(n/2))
z=np.fft.fftshift(Y)
plotter(f,z)
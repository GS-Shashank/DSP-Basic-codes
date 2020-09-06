"""
    SINE, COSINE, SQUARE WAVE GENERATION
    
    BY:- GSS

"""
import math
import numpy as np
import matplotlib.pyplot as plt

time= np.arange(0, 1, 0.01);
sig_freq =float(input("Enter the frequency for sine and cosine waves:\t"))

#plotting Sine wave 
amplitude_sine = np.sin(2*math.pi*sig_freq*time)
plt.plot(time, amplitude_sine)
plt.title('Sine wave')
plt.xlabel('Time')
plt.ylabel('Amplitude ')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.show()

#plotting the cosine wave
amplitude_cosine = np.cos(2*math.pi*sig_freq*time)
plt.plot(time, amplitude_cosine)
plt.title('Cosine wave')
plt.xlabel('Time')
plt.ylabel('Amplitude ')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.show()

#plotting the square wave
#frequency parameter is not used to plot the square wave
from scipy import signal as sg
time= np.arange(0,10*2*np.pi, 0.01)
signal = sg.square(time)
plt.plot(time, signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()


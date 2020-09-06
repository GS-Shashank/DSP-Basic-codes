# -*- coding: utf-8 -*-
"""
#####################################
    High Pass Filter Design
    
    Code by: GSS
    
#####################################


// Design a high pass FIR filter for the following specifications:
// Pass band edge frequency = 2500 Hz
// Stop band edge frequency = 1500 Hz
// Stopband attenuation = 40 db
// Sampling rate= 8000Hz

// ---------------------------------------------------------------------------------------
// Window                  Stopband attenuation       Transition width = |fs-fp|/fsamp (Hz)
// ---------------------------------------------------------------------------------------
// Rectangular window         21 dB                   0.9/N
// Bartlett window            25 dB                   
// Hanning window             44 dB                   3.1/N
// Hamming window             53 dB                   3.3/N
// Blackmann window           74 dB                   5.5/N
// ---------------------------------------------------------------------------------------


"""
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy import signal


fp=2500
fs=1500
fsamp=8000

k=3
trans_width=(fp-fs)/fsamp
N=math.ceil(k/trans_width)

if(N%2==0):
    N=N+1

hn=signal.firwin(N,2*(fp/fsamp),pass_zero="highpass",window='hamming')
M=1024;
ex=np.zeros(M-len(hn))
hn=np.concatenate([hn,ex])
H=np.fft.fft(hn)


H_Mag=20*(np.log10(np.abs(H)))

H_ang=[]

for i in range(M):
    H_ang.append(math.atan2(H[i].imag,H[i].real))
    
H_phase=((np.unwrap(H_ang)*180)/math.pi)
f=np.arange(0,(M/2)-1)*(fsamp/M)

end=int(M/2)-1

#Plotting the magnitude response 

plt.plot(f,H_Mag[0:end])
plt.xlabel('w(Hz)')
plt.grid(1)
plt.ylabel('Magnitude(dB)')
plt.title('Magnitude Response')
plt.show()


#Plotting the Phase response 
plt.plot(f,H_phase[0:end])
plt.xlabel('w(Hz)')
plt.ylabel("Phase(Deg)")
plt.title("Phase Response")
plt.grid(1)
plt.show()



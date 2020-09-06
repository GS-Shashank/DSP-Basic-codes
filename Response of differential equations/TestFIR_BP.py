# -*- coding: utf-8 -*-
"""
#####################################
    Band Pass Filter Design
    
    Code by: GSS
    
#####################################
// Design a band pass FIR filter for the following specifications:
// Pass band frequency = 1600-2300 Hz
// Lower Stop band edge frequency = 500 Hz
// Upper Stop band edge frequency = 3500 Hz
// Stopband attenuation = 50 db
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


fp_low=1600
fp_high=2300
fs_low=500
fs_high=3500
fsamp=8000


k=3.3
trans_width_low=(fp_low-fs_low)/fsamp
N1=math.ceil(k/trans_width_low)
trans_width_high=(fs_high-fp_high)/fsamp
N2=math.ceil(k/trans_width_high)

N=max(N1,N2)

if(N%2==0):
    N=N+1

hn=signal.firwin(N,[(fp_low/fsamp)*2,(fp_high/fsamp)*2],pass_zero="bandpass",window='hamming')
M=1024
ex=np.zeros(M-len(hn))
hn=np.concatenate([hn,ex])
H=np.fft.fft(hn)

H_Mag=20*(np.log10(np.abs(H)))

H_ang=[]
for i in range(M):
    H_ang.append(math.atan2(H[i].imag,H[i].real))
    
f=np.arange(0,(M/2)-1)*(fsamp/M)
H_phase=((np.unwrap(H_ang)*180)/math.pi)

end=int(M/2)-1

#Plotting the magnitude response 
plt.plot(f,H_Mag[0:end])
plt.xlabel('w(Hz)')
plt.ylabel('Magnitude(dB)')
plt.title('Magnitude Response')
plt.grid(1)
plt.show()


#Plotting the Phase response 
plt.plot(f,H_phase[0:end])
plt.xlabel('w(Hz)')
plt.ylabel("Phase(Deg)")
plt.title("Phase Response")
plt.grid(1)
plt.show()



"""
    Convolution of two signals
    
    code by: GSS

"""

# Program to compute the convolution of two sequences without using the bulitin function conv()
# User should enter the input sequence, impulse response  
# Convolution is computed using the corresponding formula 
# The computed convolved sequence sholud be displayed and cross checked 

#importing the required libraries
import numpy as np
from scipy import signal

#taking input from the User 
x=list(map(int,input('Enter the first sequence:').strip().split()))
h=list(map(int,input('Enter the second sequence:').strip().split()))

x_len=len(x)
h_len=len(h)
y_len=x_len+h_len-1

#concatenation
a=np.concatenate((x,np.zeros(h_len)))
b=np.concatenate((h,np.zeros(x_len)))
y=np.zeros(y_len)


for i in range(y_len):
    y[i]=0
    for j in range(i+1):
        y[i]=y[i]+a[j]*b[i-j]
#output        
print("Convolution using the formula  is given by:\t",y)
print("Convolution using the builtin function is given by:\t",signal.convolve(x,h))
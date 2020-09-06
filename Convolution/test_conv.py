"""
#############################
    Convolution Testing
    
    code by: GSS
#############################    
    
Program to compute the convolution of two sequences

User should enter the input sequence, impulse response  and the range of the input sequence, impulse response

Convolution is computed using the bulitin function signal.convolve() 

The input sequence, impulse response and convolved sequence sholud be plotted

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#taking input sequence 1 from user

x=list(map(int,input('Enter the first sequence:').strip().split()))
xa,xb=map(int,input('Enter the range separated by ":"(for Eg:-2:2 or 3:5):').split(":"))
nx=np.arange(xa,xb+1,1)

#taking input sequence 2 from user

h=list(map(int,input('Enter the second sequence:').strip().split()))
ha,hb=map(int,input('Enter the range separated by ":"(for Eg:-2:2 or 3:5):').split(":"))
nh=np.arange(ha,hb+1,1)

#calculating the range of the convoluted sequence

nyb=nx[0]+nh[0]
nye=nx[len(nx)-1]+nh[len(nh)-1]
ny=np.arange(nyb,nye+1,1)

#calculating the output convoluted signal
y=signal.convolve(x,h)

#plotting the input sequence 1
plt.title("First Input Sequence")
plt.xlabel("n")
plt.ylabel("x(n)")
plt.stem(nx,x,linefmt="grey",markerfmt="X")
plt.axhline(color="red", zorder=-1)
plt.axvline(color="red", zorder=-1)
plt.grid(1)
plt.show()


#plotting the input sequence 2
plt.title("Second Input Sequence")
plt.xlabel("n")
plt.ylabel("h(n)")
plt.stem(nh,h,linefmt="grey",markerfmt="X")
plt.axhline(color="red", zorder=-1)
plt.axvline(color="red", zorder=-1)
plt.grid(1)
plt.show()


#plotting the output convoluted sequence
plt.title("Convoluted Output Sequence")
plt.xlabel("n")
plt.ylabel("y(n)")
plt.stem(ny,y,linefmt="grey",markerfmt="X")
plt.axhline(color="red", zorder=-1)
plt.axvline(color="red", zorder=-1)
plt.grid(1)
plt.show()

print("The convoluted Sequence is given by:",y)



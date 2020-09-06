"""
    PROGRAM TO FIND THE RESPONSE OF THE DIFFERENTIAL EQUATION
    
    Code by: GSS

"""
 # Consider the equation
 # y(n)=0.1x(n)+0.25x(n-1)+0.2x(n-2)
 # Let us solve the difference equation for the FIR system
 # chose x(n)= delta function and find h(n)
 # chose x(n)= step function and find y(n)


from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

B=[0.1, 0.25, 0.2]
A=[1]
n=np.arange(0,10,1)
fig, (imp_resp,step_resp) = plt.subplots(2, 1, sharex=True)

# Finding the impulse response 'h(n)' from delta input
x=signal.unit_impulse(10)
y=signal.lfilter(B,A,x)
imp_resp.set(xlabel='n',ylabel='h(n)')
imp_resp.set_title("Impulse Response")
imp_resp.stem(n,y,use_line_collection=True)


# Finding the step response 'y(n)' from step input

a=np.ones(10)
b=signal.lfilter(B,A,a)
step_resp.set(xlabel='n',ylabel='y(n)')
step_resp.set_title("Step Response")
step_resp.stem(n,b,use_line_collection=True)
fig.tight_layout()
fig.show()
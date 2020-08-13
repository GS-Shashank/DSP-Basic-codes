
"""
    CROSS-CORRELATION
		This code is to verify different properties in Cross-correlation
    
    BY:- GSS

"""
import pandas as pd
import numpy as np
import math
from scipy import signal

x=[1, 4,2,3]
y=[1 ,2 ,3 ,4]

print("**************************************************************************")

rxy= signal.correlate(x,y)
ryx= signal.correlate(y,x)
rxx= signal.correlate(x,x)
ryy= signal.correlate(y,y)
print("\nrxy:",rxy,"\n\nryx:",ryx,"\n\nrxx:",rxx,"\n\nryy:",ryy)

rxxcenter=math.ceil(len(rxx)/2)
ryycenter=math.ceil(len(ryy)/2)


rxx0=rxx[rxxcenter-1]
ryy0=ryy[ryycenter-1]

print("\nrxx0=",rxx0,"\t\tryy0=",ryy0)
rxxryy0=rxx0*ryy0
rxy2=rxy*rxy

rxyinv=rxy[::-1]

def check(list1, val): 
    for z in list1: 
        if val<=z: 
            return False
    return True

if (rxyinv.all()==ryx.all()):
   
   print("**************************************************************************")

   print('Property rxy(-m)=ryx(m) is verified')


if(check(rxy2,rxxryy0)==True):

    print("**************************************************************************")

    print('Property Rxy^2<=Rxx(0).Ryy(0) is verified')


if(check(rxy,1/2*(rxx0+ryy0))==True):
    
    print("**************************************************************************")

    print('Property Rxy(m)<=1/2[Rxx(0)+Ryy(0)] is verified')
    
    print("**************************************************************************")
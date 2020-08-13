"""
    AUTO-CORRELATION
	
	This code is used to analyze different properties of auto-correltion

    Code by:- GSS
    
"""

# Let us first import all the required libraries
import numpy as np
import math
from scipy import signal
print("**************************************************************************")

#let us consider a discrete signal as shown below
x=[1,4,2,3]

#auto-coreltion function using inbuilt function in scipy
rxx=signal.correlate(x,x)
print("correlated signal:",rxx)

rxxcenter=math.floor(len(rxx)/2)

print('\nCenter position:',rxxcenter)
#deriving 'rxxleft' and 'rxxright' arrays

rxxleft=[]
rxxright=[]

for i in range(rxxcenter+1):
    rxxleft.append(rxx[rxxcenter-i])
print('\nrxx[rxxcenter]=',rxx[rxxcenter])

i=0

for i in range(rxxcenter+1):
    rxxright.append(rxx[rxxcenter+i])
print('\nrxxleft=',rxxleft)
print('\nrxxright=',rxxright)

# properties to be proved

if(rxxleft == rxxright):
    print("******************************************************")
    print("symmetry property proved")
    print("******************************************************")

def check(rxx, val): 
    for z in rxx: 
        if val< z: 
            return False
    return True
      
if(check(rxx,rxx[rxxcenter])==True):
    print("******************************************************")
    print("Upper bound property Rxx(0)>=Rxx(k) is verified")
    print("******************************************************")
##########################################################################
#or 																	##
#																		##
#i=0																	##						
# cntr=0																##
# for i in range(len(rxx)):												##
#     if(rxx[rxxcenter-1]<rxx[i]):										##
#         cntr=cntr+1													##
#																		##
# if (cntr==0):															##
#     print("******************************************************")	##
#     print("Upper bound property Rxx(0)>=Rxx(k) is verified")			##
#     print("******************************************************")	##
##########################################################################
y=np.square(x)        
mean=sum(y)

if(rxx[rxxcenter]==mean):
    print("******************************************************")
    print("Mean square value=correlation value at zero shift")
    print("******************************************************")
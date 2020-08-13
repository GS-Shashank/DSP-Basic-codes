"""
    Convolution properties
    
    code by : GSS
"""
# Program to verify the following convolution properties
#  1 Commutative Property :a[n]*b[n]=b[n]*a[n]
#  2 Associative Property :a[n]*(b[n]*c[n])=(a[n]*b[n])*c[n]
#  3 Distributive Propery :a[n]*b[n]+a[n]*c[n]=a[n]*(b[n]+c[n])
#  Note: The sequence lengths should be same.

import numpy as np
from scipy import signal


a=list(map(int,input('Enter the first sequence:').strip().split()))
b=list(map(int,input('Enter the second sequence:').strip().split()))
c=list(map(int,input('Enter the third sequence:').strip().split()))

# proof of commutative property
lhs=signal.convolve(a,b)
rhs=signal.convolve(b,a)

if(lhs.all()==rhs.all()):
    print("\nCommutative property is proved\n")
else:
    print("\nCommutative property fails\n")
    

# proof of associative property    
lhs=signal.convolve(a,signal.convolve(b,c)) 
rhs=signal.convolve(signal.convolve(a,b),c)


if(lhs.all()==rhs.all()):
    print("\nAssociative property is proved\n")
else:
    print("\nAssociative property fails\n")

# proof of distributive property
    
lhs=signal.convolve(a,b)+signal.convolve(a,c)
rhs=signal.convolve(a,np.add(b,c))


if(lhs.all()==rhs.all()):
    print("\nDistributive property is proved\n")
else:
    print("\nDistributive property fails\n")
    
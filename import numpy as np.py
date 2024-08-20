import numpy as np
import math
a=1
b=1001
c=0.0
for i in np.linspace(-a,a,b):
    for j in np.linspace(-a,a,b):
        for k in np.linspace(-a,a,b):
            c+=(math.pow(math.e,i)**2+math.pow(math.e,j)**2+math.pow(math.e,k)**2)
print (str(c))

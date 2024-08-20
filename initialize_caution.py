import numpy as np
import os
import random
os.chdir(r'C:\Users\TimeI\Desktop\new borad1')
a=np.empty([8,5,5],dtype=np.float16)
a[1]=[[-1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,-1]]
a[2]=[[0,0,-1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,-1,0,0]]
a[3]=[[0,0,0,0,0],[0,0,0,0,0],[-1,1,1,1,-1],[0,0,0,0,0],[0,0,0,0,0]]
a[4]=[[0,0,0,0,-1],[0,0,0,1,0],[0,0,1,0,0],[0,1,0,0,0],[-1,0,0,0,0]]
a[5]=[[0.6,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,0.6]]
a[6]=[[0,0,0.6,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0.6,0,0]]
a[7]=[[0,0,0,0,0],[0,0,0,0,0],[0.6,1,1,1,0.6],[0,0,0,0,0],[0,0,0,0,0]]
a[0]=[[0,0,0,0,0.6],[0,0,0,1,0],[0,0,1,0,0],[0,1,0,0,0],[0.6,0,0,0,0]]
np.save("ker_1.npy",a)
b=np.zeros([344],dtype=np.float32)
np.save("bias.npy",b)
c=np.empty([8,3,3],dtype=np.float32)
for i in np.linspace(0,7,8):
    c[int(i)]=[[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]]
np.save("ker_2.npy",c)
d_1=np.ones([8,3,3],dtype=np.float32)
d_2=np.ones([24,3,3],dtype=np.float32)
d_3=np.ones([56,3,3],dtype=np.float32)
for i in np.linspace(0,55,56):
    for j in [0,1,2]:
        for k in [0,1,2]:
            d_3[int(i)][j][k]+=random.uniform(-0.1,0.5)
np.save("ker_3_1.npy",d_1)
np.save("ker_3_2.npy",d_2)
np.save("ker_3_3.npy",d_3)
mat_1=np.ones([84,88],dtype=np.float32)
for i in np.linspace(0,83,84):
    for j in np.linspace(0,87,88):
        mat_1[int(i)][int(j)]+=random.uniform(-0.1,0.05)
np.save("mat_1.npy",mat_1)
mat_2=np.ones([169,84],dtype=np.float32)        #fully connected coff
np.save("mat_2.npy",mat_2)

import math
import numpy as np
import os
os.chdir(r'C:\Users\TimeI\Desktop\new borad1')
step=0.05
y=np.load("y.npy")
bg_5=np.load("bg_5.npy")
bg_4=np.load("bg_4.npy")
mat_2=np.load("mat_2.npy")
arr_2=np.load("bias.npy")[174:343]
mat_2c=np.zeros_like(mat_2,dtype=np.float32)
arr_2c=np.zeros_like(arr_2,dtype=np.float32)
coff_4=np.zeros([84],dtype=np.float32)
biasc=[]
for i in np.linspace(0,168,169):
    for j in np.linspace(0,83,84):
        arr_2c[int(i)]+=-step*(bg_5[int(i)]-y[int(i)])
        mat_2c[int(i)][int(j)]+=-step*bg_4[int(j)]*(bg_5[int(i)]-y[int(i)])
        coff_4[int(j)]+=mat_2[int(i)][int(j)]*(bg_5[int(i)]-y[int(i)])
np.save("mat_2c.npy",mat_2c)
biasc+=arr_2c.tolist()
mat_1=np.load("mat_1.npy")
arr_1=np.load("bias.npy")[90:174]
bg_3=np.load("bg_3.npy")
mat_1c=np.zeros_like(mat_1)
arr_1c=np.zeros_like(arr_1)
coff_3=np.zeros([88],dtype=np.float32) #dc/dbg_3
for i in np.linspace(0,83,84):
    for j in np.linspace(0,87,88):
        arr_1c[int(i)]+=-step*coff_4[int(i)]
        mat_1c[int(i)][int(j)]+=-step*coff_4[int(i)]*bg_3[int(j)]
        coff_3[int(j)]+=mat_1[int(i)][int(j)]*coff_4[int(i)]
np.save("mat_1c.npy",mat_1c)
biasc=arr_1c.tolist()+biasc
ker_3_1=np.empty([8,3,3],dtype=np.float32)
ker_3_1=np.load("ker_3_1.npy")
ker_3_2=np.empty([24,3,3],dtype=np.float32)
ker_3_2=np.load("ker_3_2.npy")
ker_3_3=np.empty([56,3,3],dtype=np.float32)
ker_3_3=np.load("ker_3_3.npy")
ker_3_1_0=np.load("bias.npy")[2:10]
ker_3_2_0=np.load("bias.npy")[10:34]
ker_3_3_0=np.load("bias.npy")[34:90]
bg_2=np.load("bg_2.npy")
coff_2=np.zeros_like(bg_2,dtype=np.float32)
ker_3_1c=np.zeros_like(ker_3_1,dtype=np.float32)
ker_3_1_0c=np.zeros_like(ker_3_1_0,dtype=np.float32)
for i in np.linspace(0,7,8):
    ker_3_1c[int(i)]+=-step*coff_3[int(i)]*bg_2[int(i)]
    ker_3_1_0c[int(i)]+=-step*coff_3[int(i)]
    coff_2[int(i)]+=ker_3_1[int(i)]*coff_3[int(i)]
ker_3_2c=np.zeros_like(ker_3_2,dtype=np.float32)
ker_3_2_0c=np.zeros_like(ker_3_2_0,dtype=np.float32)
for i in np.linspace(8,15,8):
    ker_3_2c[int(i)-8]+=-step*coff_3[int(i)]*bg_2[int(i)%8]
    ker_3_2c[int(i)-8]+=-step*coff_3[int(i)]*bg_2[int(i+1)%8]
    ker_3_2_0c[int(i)-8]+=-step*coff_3[int(i)]
    coff_2[int(i)%8]+=ker_3_2[int(i)-8]*coff_3[int(i)]
    coff_2[(int(i)+1)%8]+=ker_3_2[int(i)-8]*coff_3[int(i)]
for i in np.linspace(16,23,8):
    ker_3_2c[int(i)-8]+=-step*coff_3[int(i)]*bg_2[int(i)%8]
    ker_3_2c[int(i)-8]+=-step*coff_3[int(i)]*bg_2[int(i+2)%8]
    ker_3_2_0c[int(i)-8]+=-step*coff_3[int(i)]
    coff_2[int(i)%8]+=ker_3_2[int(i)-8]*coff_3[int(i)]
    coff_2[(int(i)+2)%8]+=ker_3_2[int(i)-8]*coff_3[int(i)]
for i in np.linspace(24,31,8):
    ker_3_2c[int(i)-8]+=-step*coff_3[int(i)]*bg_2[int(i)%8]
    ker_3_2c[int(i)-8]+=-step*coff_3[int(i)]*bg_2[int(i+3)%8]
    ker_3_2_0c[int(i)-8]+=-step*coff_3[int(i)]
    coff_2[int(i)%8]+=ker_3_2[int(i)-8]*coff_3[int(i)]
    coff_2[(int(i)+3)%8]+=ker_3_2[int(i)-8]*coff_3[int(i)]
ker_3_3c=np.zeros_like(ker_3_3,dtype=np.float32)
ker_3_3_0c=np.zeros_like(ker_3_3_0,dtype=np.float32)
l=31
series=[0,1,2,3,4,5,6,7]
for i in series:
    for j in series[i+1:]:
        for k in series[j+1:]:
            l+=1
            ker_3_3c[l-32]+=-step*coff_3[l]*bg_2[i]
            ker_3_3c[l-32]+=-step*coff_3[l]*bg_2[j]
            ker_3_3c[l-32]+=-step*coff_3[l]*bg_2[k]
            ker_3_3_0c[l-32]+=-step*coff_3[l]
            coff_2[i]+=ker_3_3[l-32]*coff_3[l]
            coff_2[j]+=ker_3_3[l-32]*coff_3[l]
            coff_2[k]+=ker_3_3[l-32]*coff_3[l]
a=ker_3_1_0c.tolist()
b=ker_3_2_0c.tolist()
c=ker_3_3_0c.tolist()
biasc=a+b+c+biasc
np.save("ker_3_1c.npy",ker_3_1c)
np.save("ker_3_2c.npy",ker_3_2c)
np.save("ker_3_3c.npy",ker_3_3c)
for i in np.linspace(0,2,3):
    for j in np.linspace(0,2,3):
        for k in np.linspace(0,7,8):
            coff_2[int(k)][int(i)][int(j)]=coff_2[int(k)][int(i)][int(j)]*bg_2[int(k)][int(i)][int(j)]*(1-bg_2[int(k)][int(i)][int(j)])
bg_1=np.load("bg_1.npy")
coff_1=np.zeros_like(bg_1,dtype=np.float32)
for i in [0,3,6]:
    for j in [0,3,6]:
        for k in [0,1,2]:
            for l in [0,1,2]:
                for m in np.linspace(0,7,8):
                    coff_1[int(m)][i+k][j+l]+=coff_2[int(m)][i//3][j//3]/9
ker_2_0c=[0]
a=[0]
biasc=a+biasc
ker_1=np.load("ker_1.npy")                        #ker1.npy, firts conv kernal
ker_1_0=np.load("bias.npy")[0]
ker_1c=np.zeros_like(ker_1,dtype=np.float32)
ker_1_0c=np.zeros_like(ker_1_0,dtype=np.float32)
bg_0=np.load("bg_0.npy")
for i in [0,1,2,3,4,5,6,7,8]:
    for j in [0,1,2,3,4,5,6,7,8]:
        for k in [0,1,2,3,4,5,6,7]:
            ker_1_0c+=-step*coff_1[k][i][j]
            ker_1c[k]+=-step*coff_1[k][i][j]*bg_0[int(i):int(i)+5,int(j):int(j)+5]
np.save("ker_1c.npy",ker_1c)
a=[ker_1_0c.tolist()]
biasc=a+biasc
np.save("biasc.npy",biasc)

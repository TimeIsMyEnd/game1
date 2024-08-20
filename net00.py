import math
import numpy as np
import csv
import os
os.chdir(r'C:\Users\TimeI\Desktop\new borad1')
board=np.load("board.npy")
Alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M']
bg_0=np.ones([2,13,13],dtype=np.int8)
bg_0[0]=board
np.save("bg_0.npy",bg_0[0])
ker_1=np.empty([8,5,5],dtype=np.float16)
ker_1=np.load("ker_1.npy")                        #ker1.npy, firts conv kernal
ker_1_0=np.load("bias.npy")[0]
#first conv start
bg_1=np.zeros([8,9,9],dtype=np.float32) #first layer
for i in np.linspace(0,8,9):
    for j in np.linspace(0,8,9):
        for k in np.linspace(0,7,8):
            bg_1[int(k)][int(i)][int(j)]=np.vdot(ker_1[int(k)],bg_0[0][int(i):int(i)+5,int(j):int(j)+5])+ker_1_0 
np.save("bg_1.npy",bg_1) 
#pooling & sigmoid                                                     #may can try tanh. should use tanh here.
bg_2=np.zeros([8,3,3],dtype=np.float32) #second layer
ker_2=np.empty([8,3,3],dtype=np.float32)
ker_2=np.load("ker_2.npy")
ker_2_0=np.load("bias.npy")[1]
for i in np.linspace(0,2,3):
    for j in np.linspace(0,2,3):
        for k in np.linspace(0,7,8):
            for l in np.linspace(0,7,8):
                bg_2[int(k)][int(i)][int(j)]+=1/(1+math.pow(math.e,-np.vdot(ker_2[int(k)],bg_1[int(l)][int(i)*3:int(i)*3+3,int(j)*3:int(j)*3+3])-ker_2_0))     #average pooling #sigmoid
np.save("bg_2.npy",bg_2)
#I call it a non-fully-connected conv
ker_3_1=np.empty([8,3,3],dtype=np.float32)
ker_3_1=np.load("ker_3_1.npy")
ker_3_2=np.empty([24,3,3],dtype=np.float32)
ker_3_2=np.load("ker_3_2.npy")
ker_3_3=np.empty([56,3,3],dtype=np.float32)
ker_3_3=np.load("ker_3_3.npy")
ker_3_1_0=np.load("bias.npy")[2:10]
ker_3_2_0=np.load("bias.npy")[10:34]
ker_3_3_0=np.load("bias.npy")[34:90]
bg_3=np.zeros([88],dtype=np.float32)
for k in np.linspace(0,7,8):
    bg_3[int(k)]=np.vdot(ker_3_1[int(k)],bg_2[int(k)])+ker_3_1_0[int(k)]
for k in np.linspace(8,15,8):
    bg_3[int(k)]=np.vdot(ker_3_2[int(k)-8],bg_2[int(k)%8])+np.vdot(ker_3_2[int(k)-8],bg_2[(int(k)+1)%8])+ker_3_2_0[int(k)-8]
for k in np.linspace(16,23,8):
    bg_3[int(k)]=np.vdot(ker_3_2[int(k)-8],bg_2[int(k)%8])+np.vdot(ker_3_2[int(k)-8],bg_2[(int(k)+2)%8])+ker_3_2_0[int(k)-8]
for k in np.linspace(24,31,8):
    bg_3[int(k)]=np.vdot(ker_3_2[int(k)-8],bg_2[int(k)%8])+np.vdot(ker_3_2[int(k)-8],bg_2[(int(k)+3)%8])+ker_3_2_0[int(k)-8]
l=32
series=[0,1,2,3,4,5,6,7]
for i in series:
    for j in series[i+1:]:
        for k in series[j+1:]:
            bg_3[l]=np.vdot(ker_3_3[l-32],bg_2[int(i)])+np.vdot(ker_3_3[l-32],bg_2[int(j)])+np.vdot(ker_3_3[l-32],bg_2[int(k)])+ker_3_3_0[l-32]
            l+=1
np.save("bg_3.npy",bg_3)
#fully connecting
mat_1=np.empty([84,88],dtype=np.float32)
mat_1=np.load("mat_1.npy")
arr_1=np.empty([84],dtype=np.float32)
arr_1=np.load("bias.npy")[90:174]
bg_4_0=np.matmul(mat_1,bg_3)
bg_4=np.empty([84],dtype=np.float32)
for i in np.linspace(0,83,84):
    bg_4[int(i)]=1/(1+math.pow(math.e,-bg_4_0[int(i)]-arr_1[int(i)]))
np.save("bg_4.npy",bg_4)
#ready to output with softmax
bg_5_1=np.empty([169],dtype=np.float64)         #e^x, ready for softmax.
mat_2=np.empty([169,84],dtype=np.float32)        #fully connected coff
mat_2=np.load("mat_2.npy")
arr_2=np.empty([169],dtype=np.float32)
arr_2=np.load("bias.npy")[174:]
bg_5_0=np.empty([169],dtype=np.float32)
bg_5_0=np.matmul(mat_2,bg_4)
for i in np.linspace(0,168,169):
    bg_5_1[int(i)]=math.pow(math.e,bg_5_0[int(i)]+arr_2[int(i)])
bg_5=np.empty([169],dtype=np.float32)
to=0
for item in bg_5_1:
    to+=item
for i in np.linspace(0,168,169):
    bg_5[int(i)]=bg_5_1[int(i)]/to
point=0
for i in np.linspace(0,168,169):
    if bg_5[int(i)]>=bg_5[point] and bg_0[0][int(i)//13][int(i)%13]==0:
        point=int(i)
np.save("bg_5.npy",bg_5)
np.save("point.npy",point)

'''for k in np.linspace(32,39,8):
    bg_3[k]=np.vdot(ker_3_3[k-32],bg_2[k])+np.vdot(ker_3_3[k-32],bg_2[k+1])+np.vdot(ker_3_3[k-32],bg_2[k+2])
for k in np.linspace(40,47,8):
    bg_3[k]=np.vdot(ker_3_3[k-32],bg_2[k])+np.vdot(ker_3_3[k-32],bg_2[k+1])+np.vdot(ker_3_3[k-32],bg_2[k+3])
for k in np.linspace(48,55,8):
    bg_3[k]=np.vdot(ker_3_3[k-32],bg_2[k])+np.vdot(ker_3_3[k-32],bg_2[k+1])+np.vdot(ker_3_3[k-32],bg_2[k+4])
for k in np.linspace(56,63,8):
    bg_3[k]=np.vdot(ker_3_3[k-32],bg_2[k])+np.vdot(ker_3_3[k-32],bg_2[k+2])+np.vdot(ker_3_3[k-32],bg_2[k+4])
for k in np.linspace(64,71,8):
    bg_3[k]=np.vdot(ker_3_3[k-32],bg_2[k])+np.vdot(ker_3_3[k-32],bg_2[k+2])+np.vdot(ker_3_3[k-32],bg_2[k+3])
for k in np.linspace(72,79,8):
    bg_3[k]=np.vdot(ker_3_3[k-32],bg_2[k])+np.vdot(ker_3_3[k-32],bg_2[k+3])+np.vdot(ker_3_3[k-32],bg_2[k+4])'''
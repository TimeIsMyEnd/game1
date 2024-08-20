import math
import numpy as np
import csv
import os
def check(board,x,y):
    win=0
    print(board[y][x])
    for i in [y-1,y,y+1]:
        for j in [x-1,x,x+1]:
            if ((i!=y)or(j!=x)) and i>=0 and j>=0 and i<=12 and j<=12:
                if board[i][j]==board[y][x]: 
                    print(str(x),str(y),str(i),str(j))
                    win=dog(board,x,y,i,j)
    return win
def dog(board,x,y,i,j):
    count=-1
    s=0
    t=0
    arr=[i-y,j-x]
    while y+s>=0 and x+t>=0 and y+s<=12 and x+t<=12:
        if board[int(y+s)][int(x+t)]!=board[y][x]:
            break 
        count+=1
        print(str(s),str(t),board[y+s][x+t],board[y][x])
        s+=arr[0]
        t+=arr[1]
    s=0
    t=0
    while y+s>=0 and x+t>=0 and y+s<=12 and x+t<=12:
        if board[int(y+s)][int(x+t)]!=board[y][x]:
            break 
        count+=1
        s-=arr[0]
        t-=arr[1]
    if count>=5:
        return board[y][x]
#input("press enter to start")
os.chdir(r'C:\Users\TimeI\Desktop\new borad1')
board=np.zeros([13,13],dtype=np.int8)
np.save("board.npy",board)
Alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M']
history_0=np.zeros([169,2,13,13],np.int8)
history_1=np.empty([169,8,9,9],np.float32)
history_2=np.empty([169,8,3,3],np.float32)
history_3=np.empty([169,88],np.float32)
history_4=np.empty([169,84],np.float32)
history_5=np.empty([169,169],np.float32)
np.save("history_0",history_0)
np.save("history_1",history_1)
np.save("history_2",history_2)
np.save("history_3",history_3)
np.save("history_4",history_4)
np.save("history_5",history_5)

steps=0
color=input("if you want hold black type x, white type o")
if color=='o':
    board[6][6]=1
    q=1
    for i in np.linspace(0,167,1698):
        history_0[int(i)+1][0][6][6]=1
    history_0[0][1][6][6]=1
    steps=1
    np.save("board.npy",board)
else:
    q=-1    #will be used to invert the board
alpha='   A B C D E F G H I J K L M'
while True:
    print(alpha)
    j=0
    for i in board:
        j+=1
        line=str(j)
        if j<=9:
            line=line+' '
        for k in [0,1,2,3,4,5,6,7,8,9,10,11,12]:
            if i[k]==q*1:
                line+=' x'
            elif i[k]==q*(-1):
                line+=' o'
            else: line+='  '
        print (line)

    new=input("write your desired coordinate in form like A12")
    x=Alphabet.index(new[0])
    y=int(new[1:])-1
    while board[y][x]!=0:
        new=input("impossible! Write your desired coordinate in form like A12")
        x=Alphabet.index(new[0])
        y=int(new[1:])-1
    board[y][x]=-1
    for i in np.linspace(steps,167,167-steps+1):
        history_0[int(i)+1][0][y][x]=-1
    history_0[steps][1][y][x]=-1
    if check(board,x,y)==-1:
        win=-1
        print(' you win ')
        break
    steps+=1
    print('1')
    np.save("board.npy",board)
    os.chdir(r'C:\Users\TimeI\Desktop\new borad1\dist')
    os.system("net00.exe")
    os.chdir(r'C:\Users\TimeI\Desktop\new borad1')
    point=np.load("point.npy")
    y=point//13
    x=point%13
    board[y][x]=1
    print('(',x,y,')')
    for i in np.linspace(steps,167,167-steps+1):
        history_0[int(i)+1][0][y][x]=1
    history_0[steps][1][y][x]=1
    history_1[steps]=np.load("bg_1.npy")
    history_2[steps]=np.load("bg_2.npy")
    history_3[steps]=np.load("bg_3.npy")
    history_4[steps]=np.load("bg_4.npy")
    history_5[steps]=np.load("bg_5.npy")
    if check(board,x,y)==1:
        win=1
        print(' you lose ')
        break
    steps+=1
    np.save("board.npy",board)
np.save("playercolor_steps_win.npy",[color,steps,win])
np.save("history_0",history_0)
np.save("history_1",history_1)
np.save("history_2",history_2)
np.save("history_3",history_3)
np.save("history_4",history_4)
np.save("history_5",history_5)

    

    
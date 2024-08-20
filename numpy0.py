import math
import numpy as np
import csv
def eval(boardc):
    po = np.zeros([9,9,2], dtype=np.int8)
    g=-1
    for k in boardc:
        g+=1
        h=-1
        for l in ['A','B','C','D','E','F','G','H','I']:
            g+=1
            po[g,l,1]=np.int8(k[l])
    po0= np.ravel(po[0:8,0:8,1], order='C')
    po10= np.empty([3,3], dtype=np.float16)
    with open('go10.csv', "r") as csvfile:
        po01=csv.reader(csvfile)
    g=-1
    for rows in po01:
        g+=1
        po10[g]=np.float16(rows)
    po1= np.empty([4,4],dtype=np.float16)
    for ss in np.linspace(1,4,4):
        for tt in np.linspace(1,4,4):
            po1[ss-1,tt-1]=math.tanh(np.vdot(po10,po[2*ss-2:2*ss,2*tt-2:2*tt,1]))
    po11= np.ravel(po1, order='C')
    po211= np.empty([1,16], dtype=np.float16)
    with open('go211.csv',"r") as csvfile:
        po112=csv.reader(csvfile)
    po211= np.float16(po112)
    po212= np.empty([1,16], dtype=np.float16)
    with open('go212.csv',"r") as csvfile:
        po121=csv.reader(csvfile)
    po212= np.float16(po121)
    po201= np.inner(po211,po11)
    po202= 1/(1+math.pow(math.e,-np.inner(po212,po11)))
    return po202

with open('board.csv', "r") as csvfile:
    board=csv.DictReader(csvfile)
go = np.empty([9,9,2], dtype=np.int8)
p=-1
for j in board:
    p+=1
    q=-1
    for i in ['A','B','C','D','E','F','G','H','I']:
        q+=1
        go[p,q,1]=np.int8(j[i])
go0= np.ravel(go[0:8,0:8,1], order='C')
go10= np.empty([3,3], dtype=np.float16)
with open('go10.csv', "r") as csvfile:
    go01=csv.reader(csvfile)
i=-1
for row in go01:
    i+=1
    go10[i]=np.float16(row)
go1= np.empty([4,4],dtype=np.float16)
for s in np.linspace(1,4,4):
    for t in np.linspace(1,4,4):
        go1[i,j]=math.tanh(np.vdot(go10,go[2*s-2:2*s,2*t-2:2*t,1]))
go11= np.ravel(go1, order='C')
go211= np.empty([1,16], dtype=np.float16)
with open('go211.csv',"r") as csvfile:
    go112=csv.reader(csvfile)
go211= np.float16(go112)
go212= np.empty([1,16], dtype=np.float16)
with open('go212.csv',"r") as csvfile:
    go121=csv.reader(csvfile)
go212= np.float16(go121)
go201= np.inner(go211,go11)
go202= 1/(1+math.pow(math.e,-np.inner(go212,go11)))
def ruster(a,b):
    lm=['A','B','C','D','E','F','G','H','I']
    with open('board.csv',"r+") as csvfile:
        board=csv.DictReader(csvfile)
    board[a[0],lm[a[1]]]=b
def learn(r):
    lm=['A','B','C','D','E','F','G','H','I']
    u=(go202-r)*go202*(1-go202)*0.1
    with open('go212c.csv',"r+") as csvfile:
        go212c=csv.reader(csvfile)
    with open('go10c.csv',"r+") as csvfile:
        go10c=csv.reader(csvfile)
    rst=-1
    for item in go212:
        rst+=1
        go212c[rst]=item-u*go11[rst]
        for rtt in np.linspace(0,2,3):
            for rss in np.linspace(0,2,3):
                go10c[rtt,rss]=go10[rtt,rss]-u*go11[rst]/8*(go1[rst//4,rst%4]+1)/(math.pow(math.e,2*go[rtt+(rst//4)*2,rss+(rst%4)*2,1]+1))*go[rtt+(rst//4)*2,rss+(rst%4)*2,1]
def guinit():
    lm=['A','B','C','D','E','F','G','H','I']
    with open('boardc.csv',"r+") as csvfile:
        boardc=csv.DictReader(csvfile)
    with open('board.csv',"r+") as csvfile:
        board=csv.DictReader(csvfile)
    for ps in np.linspace(0,8,9):
        for pt in np.linspace(0,8,9):
            boardc[ps,lm[pt]]=board[ps,lm[pt]]
def guess():
    guinit()
    lm=['A','B','C','D','E','F','G','H','I']
    with open('boardc.csv',"r+") as csvfile:
        boardc=csv.DictReader(csvfile)
    ps0=0
    pt0=0
    valg=0
    for ps in np.linspace(0,8,9):
        for pt in np.linspace(0,8,9):
            c=check([ps,pt],boardc)
            if c!=0:
                d=eval(boardc)
                if d > valg:
                    ps0=ps
                    pt0=pt
                    valg=d
                guinit()
    return [ps0,pt0]
def check( ui,boardc ):
    ro=np.zeros([9,9,2], dtype=np.int8)
    g=-1
    for k in boardc:
        g+=1
        h=-1
        for l in ['A','B','C','D','E','F','G','H','I']:
            g+=1
            ro[g,l,1]=np.int8(k[l])
    ut=0
    if ro[ui[0],ui[1],1]==0:
        ro[ui[0],ui[1],1]=1
        if ui[0]==8:
            if ui[1]==8:
                if ro[ui[0]-1,ui[1]]!=0:
                    erasure([ui[0]-1,ui[1]],ro)
                if ro[ui[0],ui[1]-1]!=0:
                    erasure([ui[0],ui[1]-1],ro)
            elif ui[1]==0:
                if ro[ui[0]-1,ui[1]]!=0:
                    erasure([ui[0]-1,ui[1]],ro)
                if ro[ui[0],ui[1]+1]!=0:
                    erasure([ui[0],ui[1]+1],ro)
            else:
                if ro[ui[0]-1,ui[1]]!=0:
                    erasure([ui[0]-1,ui[1]],ro) 
                if ro[ui[0],ui[1]+1]!=0:
                    erasure([ui[0],ui[1]+1],ro)
                if ro[ui[0],ui[1]-1]!=0:
                    erasure([ui[0],ui[1]-1],ro)
        elif ui[0]==0:
            if ui[1]==8: 
                if ro[ui[0]+1,ui[1]]!=0:
                    erasure([ui[0]+1,ui[1]],ro)
                if ro[ui[0],ui[1]-1]!=0:
                    erasure([ui[0],ui[1]-1],ro)
            elif ui[1]==0: 
                if ro[ui[0],ui[1]+1]!=0:
                    erasure([ui[0],ui[1]+1],ro)
                if ro[ui[0]+1,ui[1]]!=0:
                    erasure([ui[0]+1,ui[1]],ro)
            else: 
                if ro[ui[0],ui[1]+1]!=0:
                    erasure([ui[0],ui[1]+1],ro)
                if ro[ui[0]+1,ui[1]]!=0:
                    erasure([ui[0]+1,ui[1]],ro)
                if ro[ui[0],ui[1]-1]!=0:
                    erasure([ui[0],ui[1]-1],ro)
        else:
            if ui[1]==8:
                if ro[ui[0]-1,ui[1]]!=0:
                    erasure([ui[0]-1,ui[1]],ro) 
                if ro[ui[0]+1,ui[1]]!=0:
                    erasure([ui[0]+1,ui[1]],ro)
                if ro[ui[0],ui[1]-1]!=0:
                    erasure([ui[0],ui[1]-1],ro)
            if ui[1]==0:
                if ro[ui[0]-1,ui[1]]!=0:
                    erasure([ui[0]-1,ui[1]],ro) 
                if ro[ui[0],ui[1]+1]!=0:
                    erasure([ui[0],ui[1]+1],ro)
                if ro[ui[0]+1,ui[1]]!=0:
                    erasure([ui[0]+1,ui[1]],ro)
            else:
                if ro[ui[0]-1,ui[1]]!=0:
                    erasure([ui[0]-1,ui[1]],ro) 
                if ro[ui[0],ui[1]+1]!=0:
                    erasure([ui[0],ui[1]+1],ro)
                if ro[ui[0]+1,ui[1]]!=0:
                    erasure([ui[0]+1,ui[1]],ro)
                if ro[ui[0],ui[1]-1]!=0:
                    erasure([ui[0],ui[1]-1],ro)
    if ro[ui[0],ui[1]]==0:
        return 0
    else:
        return 1
def erasure(up,roo):
    roo
                

'''def posic(pl,boardc):
    lm=['A','B','C','D','E','F','G','H','I']
    m=1
    if boardc[pl[0],lm[pl[1]]]==0:
        if pl[0]==8:
            if pl[1]==8:
                if (boardc[pl[0]-1,lm[pl[1]]]==-1) and (boardc[pl[0],lm[pl[1]-1]]==-1):
                    m=m*0
                else:
                    m=m*1
            else:
                if pl[1]==0:
                    if (boardc[pl[0]-1,lm[pl[1]]]==-1)and(boardc[pl[0],lm[pl[1]+1]]==-1):
                        m=m*0
                    else:
                        m=m*1
                else:
                    if (boardc[pl[0]-1,lm[pl[1]]]==-1)and(boardc[pl[0],lm[pl[1]+1]]==-1)and(boardc[pl[0],lm[pl[1]-1]]==-1):
                        m=m*0
                    else:
                        m=m*1
        else:
            if pl[0]==0:
                if pl[1]==8:
                    if (boardc[pl[0]+1,lm[pl[1]]]==-1) and (boardc[pl[0],lm[pl[1]-1]]==-1):
                        m=m*0
                    else:
                        m=m*1
                else:
                    if pl[1]==0:
                        if (boardc[pl[0]+1,lm[pl[1]]]==-1)and(boardc[pl[0],lm[pl[1]+1]]==-1):
                            m=m*0
                        else:
                            m=m*1
                    else:
                        if (boardc[pl[0]+1,lm[pl[1]]]==-1)and(boardc[pl[0],lm[pl[1]+1]]==-1)and(boardc[pl[0],lm[pl[1]-1]]==-1):
                            m=m*0
                        else:
                            m=m*1
            else:
                if pl[1]==8:
                    if (boardc[pl[0]+1,lm[pl[1]]]==-1) and (boardc[pl[0],lm[pl[1]-1]]==-1) and (boardc[pl[0]-1,lm[pl[1]]]==-1):
                        m=m*0
                    else:
                        m=m*1
                else:
                    if pl[1]==0:
                        if (boardc[pl[0]+1,lm[pl[1]]]==-1)and(boardc[pl[0],lm[pl[1]+1]]==-1) and (boardc[pl[0]-1,lm[pl[1]]]==-1):
                            m=m*0
                        else:
                            m=m*1
                    else:
                        if (boardc[pl[0]+1,lm[pl[1]]]==-1)and(boardc[pl[0],lm[pl[1]+1]]==-1)and(boardc[pl[0],lm[pl[1]-1]]==-1) and (boardc[pl[0]-1,lm[pl[1]]]==-1):
                            m=m*0
                        else:
                            m=m*1
    else:
        m=m*0
    if m==0:return False
    else:return True'''


                
                
import math
import numpy as np
import csv
import os
os.chdir(r'C:\Users\TimeI\Desktop\new borad1')
with open('board.csv',"r+") as csvfile1:
    board=csv.DictReader(csvfile1)
    Alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M']
    for i in board:
        for j in np.linspace(0,12,13):
            i[Alphabet[int(j)]]='1'
board=np.zeros([13,13],dtype=np.int8)
np.save("board.npy",board)

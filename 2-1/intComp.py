import csv
import numpy as np
import math
i = 0
with open('input.txt') as openFile:
    prog = np.array(csv.reader(openFile).__next__())
    while i < math.floor((len(prog)/4)):
        if int(prog[i*4]) == 1:
            prog[int(prog[(i*4)+3])] = int(prog[int(prog[(i*4)+1])]) + int(prog[int(prog[(i*4)+2])])
        elif int(prog[i*4]) == 2:
            prog[int(prog[(i*4)+3])] = int(prog[int(prog[(i*4)+1])]) * int(prog[int(prog[(i*4)+2])])
        elif int(prog[i*4]) == 99:
            break
        else:
            print('An error has occurred')
            break
        i += 1
    print(prog)

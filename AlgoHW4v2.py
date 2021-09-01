import numpy as np

lista=np.round(np.random.normal(loc=3, scale=12, size=100)).astype(int)

my=np.array([6, -10, -12,   1,   7,  16, -25,  -4,  11,   8,  14,  21,   4,  8,  16,  19,   6,  11,  -8,  11,   6,  -9,  13,  -2,   4,   1, 10,   7,   8,   5,  22,  20,  -4,   0,  30,  15,   8,   4,  16,  5,   5,   2,   3,  25,   5,  -5,  -1,   0, -18,   0,  20,  13, -1,  16,  -5,   2,  31, -24,  -1,   1, -28,  19,  11,  -5,  -5, 12,   2,   7,  18,  20, -12,   7,  -9,  19,  10,   1,   9,  39,-12,  16,   5,  11,  24,   5, -10,  22, -10,  23, -25,   5,   7,-25,   1,   8,   4,   7, -10,  11, -23,  -5])

def maxsub(lista):
    if len(lista)==1:
        return max(0,lista[0]), max(0,lista[0]), max(0,lista[0]),lista[0]
    else:
        left=lista[:len(lista)//2]
        right=lista[len(lista)//2:]

        ltot, lbeg, lend, lsum=maxsub(left)
        rtot, rbeg, rend, rsum=maxsub(right)

        mytot=max(ltot, rtot, lend+rbeg)

        mybeg=max(lbeg, lsum+rbeg)

        myend=max(rend, rsum+lend)
    
        mysum=lsum+rsum

        return mytot, mybeg, myend, mysum

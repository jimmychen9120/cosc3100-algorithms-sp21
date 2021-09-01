import numpy as np
import random

LENGTH=4096
MASK=0xfff

def hasher2(ix):
    return (17377*ix**2>>4)&MASK, ((17377*(ix+5)**2)>>8)&MASK, ((10607*(ix+7)**2)>>2)&MASK, ((17377*(ix+9)**2)>>8)&MASK, ((10607*(ix+11)**2)>>2)&MASK

class Bloom:
    def __init__(self, LENGTH, MASK, hasher):
        self.length=LENGTH
        self.mask=MASK
        self.array=np.zeros(LENGTH, dtype=bool)
        self.hasher=hasher

    def insert(self, x):
        k, i, j, m, n=self.hasher(x)
        self.array[k]=1
        self.array[i]=1
        self.array[j]=1
        self.array[m]=1
        self.array[n]=1

    def look_up(self, x):
        k, i, j, m, n=self.hasher(x)
        if self.array[k]==1 and self.array[i]==1 and self.array[j]==1 and self.array[m]==1 and self.array[n]==1:
            return True
        else:
            return False

my_bloom=Bloom(LENGTH, MASK, hasher2)

for i in random.sample(range(my_bloom.length), 200):
    my_bloom.insert(i)

for i in range(30):
    x=random.randint(0,100000)
    print(x, my_bloom.look_up(x))


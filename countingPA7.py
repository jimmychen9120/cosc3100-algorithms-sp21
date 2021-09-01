import numpy as np
import matplotlib.pyplot as plt
import math
import random
import random as rnd

def nrm(x,y):
    return math.sqrt(x**2+y**2)

def generate_samples(nr = 100000, nr_bins=10):
    bins = [0 for i in range(nr_bins)]
    for _ in range(nr):
        x, y = random.random(), random.random()
        my_bin = int(nr_bins*nrm(x,y)/math.sqrt(2))
        bins[my_bin] += 1
    return bins

def address(key, level, split):
    a=key%(2**level)
    if a<split:
        a=key%(2**(level+1))
    return a

def run():
    buckets=[0 for _ in range(150)]
    for _ in range(100000):
        buckets[address(rnd.getrandbits(32), 7, 22)]+=1
    return buckets
    
def display(bins):
    plt.bar( range(0,len(bins)), bins)
    plt.title('Distance of a random point in [0,1]x[0,1] from origin')
    plt.show()
    
    
#display(generate_samples(nr=1000000, nr_bins = 21))
display(run())

import random
import time
"""
class Gl:
    INFTY = 2**32-1

class Vertex:
    def __init__(self, x, val = Gl.INFTY):
        self.id = x
        self.degree = val
    def __str__(self):
        return '({},{})'.format(self.id, self.degree)
    def __eq__(self, other):
        return self.degree == other.degree
    def __le__(self, other):
        return self.degree <= other.degree
    def __lt__(self, other):
        return self.degree < other.degree
    def __gt__(self, other):
        return self.degree > other.degree
    def __ge__(self, other):
        return self.degree >= other.degree
    def __ne__(self, other):
        return self.degree != other.degree
    def assign(self, val):
        self.degree = val

class PQ:
    def __init__(self):
        self.array = []

    def up(index):
        return (index+1)//2-1

    def left(index):
        return 2*index + 1

    def right(index):
        return 2*index + 2

    def __str__(self):
        return 'Contents\n'+'\n'.join([str(x) for x in self.array])+'\n'

    def __len__(self):
        return len(self.array)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        try:
            ret_val = self.array[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return ret_val

    def test_heap(self):
        for i in range(1, len(self.array)):
            if self.array[i] < self.array[PQ.up(i)]:
                return False
        return True

    def insert(self, value):
        n = len(self.array)
        self.array.append(value)
        while n>0:
            parent = PQ.up(n)
            if self.array[parent] > value:
                self.array[n], self.array[parent] = self.array[parent], self.array[n]
                n = parent
            else:
                return

    def pop(self):
        ret_val = self.array[0]
        if len(self.array) == 1:
            del self.array[-1]
            return ret_val
        last = self.array[-1]
        del self.array[-1]
        self.array[0] = last
        n=0
        while n < len(self.array):
            left = PQ.left(n)
            right = PQ.right(n)
            if right < len(self.array): #current node has two children
                if self.array[n] <= self.array[left] and self.array[n] <= self.array[right]:
                    return ret_val
                if self.array[left] >= self.array[right]:
                    m = right
                else:
                    m = left
                self.array[n], self.array[m] = self.array[m], self.array[n]
                n = m
            elif left < len(self.array):    #current node has one child
                if self.array[n] > self.array[left]:
                    self.array[n], self.array[left] = self.array[left], self.array[n]
                return ret_val
            else:   #current node has no child
                return ret_val
        return ret_val

    def find(self, vertex_number):
        for i in range(len(self.array)):
            if self.array[i].id == vertex_number:
                return i

    def gen_ran(nr):
        pq = PQ()
        for i in range(nr):
            pq.insert(Vertex(i, random.randint(0,12)))
        return pq

    def lower(self, vertex_number, new_value):
        n=self.find(vertex_number)
        self.array[n].degree=new_value
        while(n>=0):
            parent=PQ.up(n)
            if self.array[parent]>self.array[n]:
                self.array[parent], self.array[n] = self.array[n], self.array[parent]
                n=parent
            else:
                return

def gen_PQ(inDegrees_list):
    pq=PQ()
    for i in range(len(inDegrees_list)):
        pq.insert(Vertex(i, inDegrees_list[i]))
    return pq

def create_random_graph(n, edge_prob):
    for i in range(n):
        inDegrees[i]=0
    result=[[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if not i==j and random.random()<edge_prob:
                result[i].append(j)
                inDegrees[j]+=1
    return result, inDegrees
"""

#I had turned in two python files in my original turn in.
#One was with my DFS code and one was with my PQ code. Now I have combined it in this file
def create_random_graph(n, edge_prob):
    result=[[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if not i==j and random.random()<edge_prob:
                result[i].append(j)
    return result

def pretty_print(adjacency_list):
    for i in range(len(adjacency_list)):
        print(i, adjacency_list[i])

def dfs(adjacency_list):
    for vertex in range(len(adjacency_list)):
        if vertex not in grey:
            dfs_visit(vertex, adjacency_list)

def dfs_visit(vertex, adjacency_list):
    grey.append(vertex)
    for v in adjacency_list[vertex]:
        if v not in grey:
            dfs_visit(v, adjacency_list)
    black.append(vertex)
    
outputTimes=[]
average=0
for i in range(100):
    inDegrees={}
    grey=[]
    black=[]
    
    #DFS testing
    startTime=time.perf_counter()
    adjacency_list=create_random_graph(50, 0.2)
    dfs(adjacency_list)
    endTime=time.perf_counter()-startTime
    """
    #PQ testing
    startTime=time.perf_counter()
    adjacency_list, inDegrees_list=create_random_graph(50, 0.2)
    #for vertex in range(len(adjacency_list)):
    pq=gen_PQ(inDegrees_list)
    endTime=time.perf_counter()-startTime
    """
    outputTimes.append(endTime)
    average+=endTime

average=average/100
for i in outputTimes:
    print(i)
print("---")
print("avg:",average)

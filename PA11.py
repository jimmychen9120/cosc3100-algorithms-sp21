import random
import time
import decimal

def create_random_graph(n, edge_prob):
    result=[[] for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if random.random()<edge_prob:
                result[i].append(j)
                result[j].append(i)
    return result

def pretty_print(adjacency_list):
    for i in range(len(adjacency_list)):
        print(i, adjacency_list[i])

def dfs(adjacency_list):
    cycleDetect=False
    for vertex in range(len(adjacency_list)):
        if vertex not in grey:
            cycleDetect=dfs_visit(vertex, adjacency_list, vertex)
            if cycleDetect:
                break
    return cycleDetect
    
def dfs_visit(vertex, adjacency_list, parent):
    grey.append(vertex)
    inGrey=False
    for v in adjacency_list[vertex]:
        if v in grey and v!=parent:
            inGrey=True
            break
        else:
            newParent=v
            dfs_visit(v, adjacency_list, newParent)
    if inGrey:
        return inGrey
    else:
        black.append(vertex)
        return False
    
cycleProb=[]
edge_prob=[0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4]
for i in edge_prob:
    cycleFound=0
    for j in range(100000):
        grey=[]
        black=[]
        
        adjacency_list=create_random_graph(100, i)
        cycleBool=dfs(adjacency_list)

        if cycleBool:
            cycleFound+=1

    average=decimal.Decimal(cycleFound)/decimal.Decimal(100000)
    cycleProb.append(average)
    
for i in cycleProb:
    print(i)

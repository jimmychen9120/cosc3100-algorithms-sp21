import functools

#Problem 1
@functools.cache
def getChange(n):
    if n<0:
        return 0
    elif n<5:
        return 1
    else:
        return getChange(n-1) + getChange(n-5) + getChange(n-10) + getChange(n-25)

last_coin={0:0}
costs={0:0}
values=[1,5,10,25]

#Problem 2
@functools.cache
def getChange2(x,n):    #number of ways to express x with n types of coins
    if n==1:
        return 1
    return sum([getChange2(x-j*values[n-1], n-1) for j in range(x//values[n-1]+1)])

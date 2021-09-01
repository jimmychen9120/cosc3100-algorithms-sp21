import functools

#Field Goal=3
@functools.cache
def getPoints3(n):
    if n<=1:
        return 0
    elif n<=3:
        return 1
    else:
        return getPoints3(n-2) + getPoints3(n-3) + getPoints3(n-6) + getPoints3(n-7)

for i in range(1,121):
    print("Score",i,":",getPoints3(i))

#Field Goal=4
@functools.cache
def getPoints4(n):
    if n<=1 or n==3:
        return 0
    elif n<=4:
        return 1
    else:
        return getPoints4(n-2) + getPoints4(n-4) + getPoints4(n-6) + getPoints4(n-7)

for i in range(1,121):
    print("Score",i,":",getPoints4(i))

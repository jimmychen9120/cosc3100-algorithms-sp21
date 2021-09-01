from time import perf_counter

for i in range(36):
	x=0
	start_time=time.perf_counter()
	for j in range(10):
		x+=fib(i)
	duration = (time.perf_counter()-start_time)/10
	print("{:12.10f}".format(duration))

def fib(n):
	hi=1
	lo=0
	for i in n:
		temp=hi
		hi=hi+lo
		lo=temp
	return lo

def rec_fib(n):
	if n<2:
		return n
	else:
		return rec_fib(value-1)+rec_fib(value-2)

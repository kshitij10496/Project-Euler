import timeit
start = timeit.default_timer()
def LCM(n):
	num = 2520
	while 1:
		count = 0
		for i in xrange (1,n+1):
			if num % i ==0:
				count+=1
			else:
				break
		if count == n:
			return num
		else:
			num+=1

print LCM(input())

stop = timeit.default_timer()
print stop-start	
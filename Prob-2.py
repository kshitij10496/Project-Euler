def fibo(n):
    sum = 0
	a=1
	b=1
	while a < n:
		if a%2==0:
			sum = sum + a
		a,b = a+b,a
	print sum

fibo(input())

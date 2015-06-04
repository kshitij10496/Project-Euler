def prime_factors(n):
	i = 2
	if prime(n)==1:
		return n
	while n>0 and i<n:
		if n % i ==0:
			n = n/i
			div = i
			prime_factors(n)
		else:
			i+=1

	return div

def prime(n):
	for i in xrange(2,n):
		if n%i ==0:
			return 0
	return 1

num = int(raw_input())
print prime_factors(num)

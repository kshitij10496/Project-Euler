def sum_of_primes(n):
	sum = 0
	for i in xrange(2,n):
		if isPrime(i)==1:
			sum += i
	return sum

def isPrime(num):
	for i in xrange(2,num):
		if num%i == 0:
			return 0
	return 1

print sum_of_primes(input())
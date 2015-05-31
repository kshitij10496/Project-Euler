def prime_number(n):
	num = 2
	prime_count = 0
	while prime_count < n:
		if prime(num) == 1:
			prime_count += 1
		if prime_count == n:
			return num
		num += 1

def prime(n):
	for i in range (2,n):
		if n%i == 0:
			return 0
	return 1

print prime_number(input())

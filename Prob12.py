def triangle_number(n):
	return n*(n+1)/2

def factors(n):    
	count = 0
	for i in xrange(1, (int(n**0.5) + 1)):
		if n % i == 0:
			count += 2
	return count

def triangle_number_factors():
	
	return_factors = 0
	i = 1
	while return_factors <= 500:
		num = triangle_number(i)
		return_factors = factors(num)
		i += 1
	print triangle_number(i-1)

triangle_number_factors()
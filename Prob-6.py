def sum_square_difference(n):
	sum_of_squares = 0
	sum_of_numbers = 0
	for i in xrange(n+1):
		sum_of_squares += i*i
		sum_of_numbers += i
	return sum_of_numbers**2 - sum_of_squares

print sum_square_difference(input()) 

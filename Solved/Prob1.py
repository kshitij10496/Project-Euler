def multiple_sum(n):
	sum = 0
	for num in range(n):
		if num%3==0 or num%5==0:
			sum = sum + num
	print sum

multiple_sum(input())
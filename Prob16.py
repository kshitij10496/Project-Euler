def sum_digits(n):
	sum = 0
	while n > 0:
		sum += n%10
		n = n/10

	return sum

def main():
	print "Enter number :"
	a = input()
	power = input()
	num = a**power

	print sum_digits(num)

main()
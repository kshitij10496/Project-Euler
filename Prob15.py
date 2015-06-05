def counting(n):
	if n == 2:
		return 6
	count = 2
	count *= counting(n-1)
	return count

def main():
	print "Enter the order of matrix"
	N = input()
	print "Count : ", counting(N)

main()
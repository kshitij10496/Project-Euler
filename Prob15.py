def path(n):
	if n == [0,0]:
		return 1

	else:
		if n[0]>0:
			path_count += path(n[0] - 1,)
	count = 2
	count *= counting(n-1)
	return count

def main():
	print "Enter the order of matrix"
	N = input()
	print "Count : ", counting(N)

main()
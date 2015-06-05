def seq(n):
	num = n
	chain = 1
	while n > 1:
		if n % 2 == 0:
			n = n/2
		else:
			n = 3*n + 1
		chain += 1
	return chain
def main():
	chain_max = 0
	number = 0
	for i in xrange(1,1000000):
		current_chain = seq(i)
		if current_chain > chain_max:
			chain_max = current_chain
			number = i
	print "Number :", number
	print "chain :" ,chain_max

main()
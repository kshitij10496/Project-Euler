def seq(n):
	num = n
	chain = 1
	if num == 1:
		return chain
	elif num % 2 == 0:
		chain = seq(num/2) + 1
		return chain
	else:
		chain = seq (3*num + 1) + 1 
		return chain

def main():
	chain_max = 0
	for i in xrange(1,1000000):
		current_chain = seq(i)
		if current_chain > chain_max:
			chain_max = current_chain
			number = i
	print "Number :" + i

main()
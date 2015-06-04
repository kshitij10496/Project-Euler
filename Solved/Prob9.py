def Pythagorean_Triplet_Sum(sum):

	for i in xrange(1,sum):
		for j in xrange(1,sum):
			a = i
			b = j
			c = sum - i - j

			if a**2 + b**2 == c**2:
				print a , b , c,
				print "Product : ", a*b*c
	return 0

Pythagorean_Triplet_Sum(input()) 

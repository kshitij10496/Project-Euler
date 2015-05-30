def lar_palin():
	for i in xrange(10**6,10**4,-1):
		if palindrome(i)==1 and fact(i)==1:
			return i
	else:
		return 0

def fact(n):
	num = n
	factors=[]
	for i in xrange(2,num):
		if num%i ==0:
			factors.append(i)
	
	l = len(factors)
	
	if l%2==0:
		if factors[l/2-1]>100 and factors[l/2]>100 and factors[l/2]<1000 and factors[l/2-1]<1000 :
			
			return 1
		else:
			return 0
	else:
		if factors[l/2]>100 and factors[l/2]<1000 :
			
			return 1
		else:
			return 0

def palindrome(n):
	original_number = n
	reverse_number = 0
	while n > 0:
		rem = n % 10
		reverse_number = reverse_number*10 + rem
		n = n / 10
	if original_number == reverse_number:
		return 1
	else:
		return 0

print lar_palin()

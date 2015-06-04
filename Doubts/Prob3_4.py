A=600851475143
n=2
fac=[]
while(n<=int(A)):
    B=1
    while(A%n==0):
        B=0   
        A=A/n
    if(B==0):
        fac.append(n)
    n=n+1

print max(fac)
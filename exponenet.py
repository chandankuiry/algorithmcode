def exp1(a,b):
	ans=1
	while(b>0):
		ans=ans*a
		b=b-1
	return ans
print exp1(4,2)


def exp2(a,b):
	if b==1:
		return a
	else:
		return a*exp2(a,b-1)
print exp2(4,3)


def exp3(a,b):
	if b==1:
		return a
	elif b%2==0:
		return exp3(a*a,b/2)
	else:
		return a*(a**(b-1))
print exp3(4,3)
 
def g(n,m):
	x=0
	for i in range(n):
		for j in range(m):
			x=x+1
	return x

print g(3,2)
	


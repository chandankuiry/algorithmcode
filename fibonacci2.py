def fib(n):
	global numcalls
	numcalls +=1
	#print 'fib call with', n
	if n<=1:
		return 1
	else:
		return fib(n-1)+fib(n-2)
numcalls=0
n= 30
res =fib(n)
print 'fib of' ,n , '=' ,res,'numcalls ',numcalls

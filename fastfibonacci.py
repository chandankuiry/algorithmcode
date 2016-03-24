def fib2(n,memo):
	global numcalls
	numcalls += 1
	#print 'fib call with', n
	if not n in memo:
		memo[n]=fib2(n-1,memo) + fib2(n-2,memo)#here memo is a dictionary to map a number we use memo that overcome overlapping subbproblem
	return memo[n]

def fib1(n):
	memo={0:1,1:1}
	return fib2(n,memo)

numcalls=0
n=30
res=fib1(n)
print 'fib of' ,n , '=' ,res,'numcalls ',numcalls

def solve(numlegs,numheads):
	for numchick in range(0,numheads+1):
		numpig=numheads-numchick
		totallegs=4*numpig + 2*numchick
		if totallegs ==numlegs:
			return [numchick,numpig]
	return [None,None]

def farmerproblem():
	numheads=int(raw_input("Enter number of heads: "))
	numlegs=int(raw_input("Enter number of legs: "))
	numchick,numpig=solve(numlegs,numheads)
	if numpig==None:
		print "There is no solution"
	else:
		print "Number of pig: ",numpig
		print "Number of chickens: ",numchick  
farmerproblem()



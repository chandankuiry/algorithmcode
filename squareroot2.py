def squarerootBi(x,epsilon):
	""" Assumes x>=0 and epsilon > 0
	    return y s.t. y*y is within epsilon of x """
	assert x>=0,'x must be non-negative ,not ' +str(x)
	assert epsilon > 0,'epsilon must be positive,not' +str(epsilon)
	low =0
	high=max(x,1.0)
	guess =(low +high)/2.0
	ctr =1
	while abs(guess**2 - x) > epsilon and ctr <=100:
		if guess**2 <x:
			low=guess
		else:
			high =guess
		guess =(low +high)/2.0
		ctr += 1
	assert ctr<=100,"iteration count exceeded"
	print 'Bi method. num. iteration',ctr,'estimate',guess
	return guess
#HERE we didn't take squarerootbi(0.25,0.001);
#because squareroot of 1/4 didn't lie between 0 to  1/4 .because 1/2 is greater than 1/4 so it outside the boundary so it don't work for fraction .so first case high=x .but if we dealing with fraction then high will be max(x,1.0), so if i take square root of 1/4 that time high will be max(1/4,1.0) so high=1.0,so perfect answer we will get. 
squarerootBi(4.0,0.000001) 


import random
import time

def findminlist(alist):
	overallmin=alist[0]
	for i in alist:
		smallest=True
		for j in alist:
			if i>j:
				smallest=False
			
		if smallest:
			overallmin=i
	return overallmin
for listsize in range(1000,10001,1000):
	alist=[random.randrange(100000) for i in range(listsize)]
	start=time.time()
	print findminlist(alist)
	end=time.time()
	print "time taken for listsize %d is %10.7f"%(listsize,end-start) 			
			






import time,random
def findmin(alist):
	minsofar=alist[0]
	for i in alist:
		if i < minsofar:
			minsofar=i
	return minsofar
#print findmin([1,2,9,8,12,5,6])
for listsize in range(1000000,10000001,1000000):
	alist=[random.randrange(100000) for i in range(listsize)]
	start=time.time()
	print findmin(alist)
	end=time.time()
	print "time taken for listsize %d is %10.7f"%(listsize,end-start) 			
			

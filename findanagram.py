import time
def findanagram(s1,s2):
	start=time.time()
	alist=list(s2)
	
	pos1=0
	findok=True
	while pos1<len(s1) and findok:
		pos2=0
		found=False
		while pos2<len(alist) and not found:
			if s1[pos1]==alist[pos2]:
				found=True
			else:
				pos2=pos2+1
		if found:
			alist[pos2]=None
		else:
			findok=False
		pos1=pos1+1
	end=time.time()
	return findok,end-start
print "result is %r and time taken for this %10.7f"%findanagram('anagram','magrana')



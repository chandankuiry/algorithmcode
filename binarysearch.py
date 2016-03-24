# simple search
def search(s,e):
	answer=None
	i=0
	numcompares=0
	while i<len(s) and answer==None:
		numcompares +=1
		if e == s[i]:
			answer=True
		elif e<s[i]:
			answer=False
		i += 1
	print answer, numcompares

# binary search
def bsearch(s,e,first,last):	
	print first,last
	if last-first < 2:
		return s[first]==e or s[last]==e
	mid=first+(last-first)/2
	if s[mid]==e:
		return True
	if s[mid] > e:
		return bsearch(s,e,first,mid-1)
	return bsearch(s,e,mid+1,last)
def search1(s,e):
	print bsearch(s,e,0,len(s)-1)
	print "search complete"



def testsearch():
	s=range(0,10000000)
	raw_input("basic search ")
	search(s,-1)
	raw_input("binary search")
	search1(s,-1)
	raw_input("basic search ")
	search(s,100000)
	raw_input("binary search 10000000")
	search1(s,1000000)

print testsearch()

	

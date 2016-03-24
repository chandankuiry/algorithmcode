# here s is sorted
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
s=[1,2,3,4,5,9,10,15,19,20,23,50]
search(s,29) 

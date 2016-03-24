def bubblesort(l):
	for j in range(len(l)):
		for i in range(len(l) - 1):
			if l[i] > l[i+1]:
				temp= l[i]
				l[i]=l[i+1]
				l[i+1] = temp
		print l
l=[1,5,2,9,6,2]
bubblesort(l)

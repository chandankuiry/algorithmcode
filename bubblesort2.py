def bubblesort(l):
	swapped =True
	while swapped:
		swapped=False
		for i in range(len(l) - 1):
			if l[i] > l[i+1]:
				temp=l[i]
				l[i] = l[i+1]
				l[i+1] =temp
				swapped =True
		print l

test1=[1,3,2,8,5,6,1,2,7,9,4]
bubblesort(test1)
				
					

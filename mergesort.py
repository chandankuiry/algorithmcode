def merge(left,right):
	""" assume left and right are sorted list.return the same list containing left+right together"""
	result=[]
	i,j=0,0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i +=1
		else:
			result.append(right[j])
			j +=1
	while i < len(left):
		result.append(left[i])
		i +=1
	while j < len(right):
		result.append(right[j])
		j +=1
	return result


def mergesort(l):
	"""return a new sort list containing the same element as l"""
	print l
	if len(l) < 2:
		return l[:]#here we print whole list
	else:
		middle=len(l) / 2
		left=mergesort(l[:middle])
		right=mergesort(l[middle:])
		together=merge(left,right)
		print "merged", together
		return together

test1=[1,3,2,8,5,6,1,2,7,9,4]
mergesort(test1)

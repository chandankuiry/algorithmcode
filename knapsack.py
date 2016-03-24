def maxvalue(w , v , i , aw):
	""" here w is weight of element , value of element, i is value is take or not, aw is available weight i have to take"""
	global numcalls
	numcalls +=1
	if i==0:
		if w[i] <= aw: return v[i]
		else: return 0
	without_i=maxvalue(w,v,i-1,aw)
	if w[i] > aw:
		return without_i
	else:
		with_i=v[i] +maxvalue(w,v,i-1,aw - w[i])
	return max(with_i,without_i)
weight=[1,5,3,4,9,5,2,1,6,5]
vals=[15,10,9,5,6,11,12,2,8,3]
numcalls=0
res =maxvalue(weight,vals,len(vals) -1, 15)
print 'maxvalue = ',res,' number of calls = ',numcalls
# in above code take time because same calls happen over and over again means we have to overcome overlapping subproblem


def fastmaxvalue(w , v , i , aw,m):
	""" here w is weight of element , value of element, i is value is take or not, aw is available weight we have to take, and m is memo which save the determined value"""
	global numcalls
	numcalls +=1
	try: return m[(i,aw)]
	except KeyError:
		if i==0:
			if w[i] <= aw:
				m[(i,aw)]=v[i]
			 	return v[i]
			else:
				m[(i,aw)]=0
				return 0
		without_i=fastmaxvalue(w,v,i-1,aw,m)
		if w[i] > aw:
			m[(i,aw)]=without_i
			return without_i
		else:
			with_i=v[i] +fastmaxvalue(w,v,i-1,aw - w[i],m)
		res = max(with_i,without_i)
		m[(i,aw)]=res
		return res

def maxval1(w,v,i,aw):
	m ={}
	return fastmaxvalue(w , v , i , aw,m)

weight=[1,5,3,4,9,5,2,1,6,5]
vals=[15,10,9,5,6,11,12,2,8,3]
numcalls=0
res =maxval1(weight,vals,len(vals) -1, 15)
print 'maxvalue = ',res,' number of calls = ',numcalls

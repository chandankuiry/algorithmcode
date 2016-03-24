def readfloat(requestmsg,errormsg):
	while True:
		val =raw_input(requestmsg)
		try:
			val =float(val)
			return val
		except:
			print(errormsg) 
#print readfloat('enter a float','it is not a number')

def readval(valtype,requestmsg,errormsg):
	while True:
		val =raw_input(requestmsg)
		try:
			val=valtype(val)
			return val
		except:
			print(errormsg)
print readval(str,'enter a float','it is not a number')

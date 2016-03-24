def getFloat(requestmsg,errormessage):
	inputok=False
	while not inputok:
		val=input(requestmsg)
		if type(val)==type(1.0):
			inputok=True
		else:
			print(errormessage)
	return val

getFloat("enter value: ","input is not afloat")

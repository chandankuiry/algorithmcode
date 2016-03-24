from stackdefine import Stack 


def converter(decimalnum,base):
	digit="0123456789ABCDEF"
	s=Stack()


	while decimalnum > 0:
		rem = decimalnum % base
		s.push(rem)
		decimalnum = decimalnum // base



	newstring = ""
	while not s.isEmpty():
		newstring= newstring + digit[s.pop()]
	return newstring

print converter(25,7)
print converter(26,26)




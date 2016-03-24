from stackdefine import Stack 


def divideBy1(decimalnum):
	s=Stack()

	while decimalnum > 0:
		rem = decimalnum % 2
		s.push(rem)
		decimalnum = decimalnum // 2



	binString = ""
	while not s.isEmpty():
		binString= binString + str(s.pop())
	return binString

print divideBy1(42)


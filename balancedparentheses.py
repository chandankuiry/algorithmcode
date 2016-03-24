from stackdefine import Stack
def parchecker(symbolstring):
	s=Stack()
	balanced=True
	index=0
	while index< len(symbolstring) and balanced:
		symbol=symbolstring[index]
		if symbol=='(' :
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced = False
			else:
				s.pop()
		index=index + 1
	if balanced and s.isEmpty():
		return True
	else:
		return False
print parchecker('((())))')
print parchecker('((()))')

def parchecker2(symbolstring):
	s=Stack()
	balanced=True
	index=0
	while index < len(symbolstring) and balanced:
		symbol=symbolstring[index]
		if symbol in '[{(':
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced=False
			else:
				top=s.pop()
				if not matches(top,symbol):
					balanced=False
		index = index  + 1

	if s.isEmpty and balanced:
		return True
	else:
		return False
def matches(open ,close):
	opens ="[{("
	closes="]})"
	return opens.index(open)==closes.index(close)

print parchecker2('{{([][])}()}')
		



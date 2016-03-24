from dequedefine import Deque 

def palindromecheck(palindromestring):
	if type(palindromestring) != str:
		raise Exception('"input must be string"')
	palindromedeque= Deque()
	for i in palindromestring:
		palindromedeque.addRear(i)

	stillok= True
	while palindromedeque.size() > 1 and stillok:
		first=palindromedeque.removeRear()
		last=palindromedeque.removeFront()
		if first != last:
			stillok=False
	return stillok

print palindromecheck("abbca")
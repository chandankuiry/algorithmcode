try:
	def squarert(x):
		"""Return Square root of x, if x is a perfect square root.Print an error message and return none othrewise""" 
	
  
		
		if type(x) == int or type(x) == float:	
			ans =0
			if x>=0:
				while ans*ans <x:
					ans=ans+1
				if ans*ans !=x:
					print x, "is not a square root number"
					return None
				else:
					return ans
			else:
				print x, "is a negative number"
				return None
		else :	
			print x, "is not a number"
			return None
except NameError:
	print  " variable is not defined "

print squarert(a)

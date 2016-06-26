class Rational(object):
	def __init__(self, numerator=0, demoniator=1):
		self.numer = numerator
		self.denom = demoniator
		self.fixSign()
		self.reduce()
	def __add__(self,rhs):  #self and rhs are Rational objects
		n1 = self.numer	#numerator of the self object
		d1 = self.denom	#denominator of the self object
		n2 = rhs.numer	 #numerator of the rhs object
		d2 rhs.denom	   #denominator of the rhs object
		r = Rational(d2*n1+d1*n2,d1*d2)	#creates a new object with d2*n1+d1*n2 as the numerator, and d1*d2 as the denominator
		return r
	def __sub__(self,rhs):
		n1 = self.numer	#numerator of the self object
		d1 = self.denom	#denominator of the self object
		n2 = rhs.numer	 #numerator of the rhs object
		d2 = rhs.denom	   #denominator of the rhs object
		r = Rational(d2*n1-d1*n2,d1*d2)	#creates a new object with d2*n1-d1*n2 as the numerator, and d1*d2 as the denominator
		return r
	def gcd(self,a,b):
		if b == 0:
			return a
		return self.gcd(b,a%b)
	def fixSigns(self):	#takes - sign out of the denominator
		if self.denom <0:	#check if denominator is negative
			self.numer = -self.numer	#switch sign of numerator
			self.denom = -self.denom	#switch sign of denominator
	def reduce(self):	#reduce the fraction
		d = 1
		if self.denom != 0 and self.numer !=0:	  #make sure the fraction != 0
			d = self.gcd(self.numer, self.denom)	#finds the greatest common denominator in order to reduce 
		if d > 1:		#reduce away!
			self.numer /= d
			self.denom /= d
	def __str__(self):			#rules for printing our objects
		s = "%d /% d" % (self.numer,self.denom)
		return s

from operator_overloading_class import *# see the operator_overloading_class in algorithmcode-in-python
def main():
	r1 = Rational(4,9)
	r2 = Rational(2,7)
	r3 = Rational(1,3)
	r4 = Rational(4,6)


	#use our __str__ function
	print "r1: ", r1
	print "r2: ", r2
	print "r3: ", r3
	print "r4: ", r4

	#use our operators

	print "r2-r1: ", (r2-r1)
	print "r1+r3: ", (r1+r3)

	r5 = r3+r4
	print r3, " + ", r2, " = ", r3

	a,b,c,d = 1,4,3,6
	print "%d/%d + %d/%d = %s" %(a,b,c,d,Rational(a,b) + Rational(c,d))
	print "%d/%d - %d/%d = %s" %(a,b,c,d,Rational(a,b) - Rational(c,d))

if __name__ == "__main__":
	main()

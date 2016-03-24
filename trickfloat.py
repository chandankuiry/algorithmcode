import math
#get base
#here we use inputok to avoid infinite loop
inputok=False
while not inputok:
	base =input("enter base: ")
	# herewe use a trick to check base is float or not 
	if type(base)==type(1.0):
		inputok=True
	else:
		print "base should be floating point number" 

#get height
inputok=False
while not inputok:
	height=input("enter height: ")
	if type(height)==type(1.0):
		inputok=True
	else:
		print "height should be floating point number" 
hyp=math.sqrt(base*base + height*height)
print hyp 

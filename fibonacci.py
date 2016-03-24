def fibonacci(x):
	#fibonacci is a history of rabbit birth after 12 month how many rabbit born
	if x==0 or x==1:
		return 1
  	else:
		return fibonacci(x-1) +fibonacci(x-2)
print fibonacci(24)

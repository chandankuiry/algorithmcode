def ispalindrome(s):
	# it is base case 
	if len(s)<=1:
		return True
	else:
		# here we check		
		return s[0]==s[-1] and ispalindrome(s[1:-1])
print ispalindrome('abccba')
#to see the indent of an palindrome we write the below code
def ispalindrome1(s,indent):
	print indent,'ispalindrome call with',s
	if len(s)<=1:
		print indent,"about to return base case"
		return True
	else:
		ans = s[0]==s[-1] and ispalindrome1(s[1:-1],indent+indent)
		print indent,"about to return ",ans
		return ans  
print ispalindrome1('abcddcba',' ')		

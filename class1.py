class Person(object):

	def __init__(self, family_name, first_name):
		self.family_name =family_name
		self.first_name =first_name
	def familyName(self):
		return self.family_name
	def firstName(self):
		return self.first_name
	def __cmp__(self,other):
		return cmp((self.family_name,self.first_name),(other.family_name,other.first_name))
	def __str__(self):
		return '<person: %s %s>'%(self.first_name,self.family_name)
	def say(self,toWhom,something):
		return self.first_name + ' ' + self.family_name + ' says to' +toWhom.first_name + ' ' +self.something
	def sing(self,toWhom,something):
		return self.say(toWhom,something + 'tr a tra ')

# here we inherit from person superclass
class  Mitperson(Person):
	nextIdnum = 0
	def __init__(self, familyName,firstName):
		Person.__init__(self, familyName,firstName)
		self.idNum=Mitperson.nextIdnum
		Mitperson.nextIdnum +=1
		#here idNum does that when we create an instance of that class tthat time
		# we give to value after that if i create another instance then it value increase like
		# per1 =Mitperson() here per1 idNum will be 0
		#after that if we create another insatnce  like per2 = Mitperson() that time per2 idNum will be  1.
		#we get the value from per1.getIdNum method
	def getIdNum(self):
		return self.idNum
	def __str__(self):
		return '< Mit Person: %s %s>' %(self.first_name,self.family_name)
	def __cmp__(self,other):
		return cmp(self.idNum ,other.idNum)
#in this class we can access say() method like per=Mitperson ,per.say() because we inherit the class from Person class
#here is the class which is inherit from Mitperson class 


class UG(Mitperson):
	def __init__(self,familyName,firstName):
		Mitperson.__init__(self,familyName,firstName)
		self.year =None
	def setYear(self,year):
		if year>5: raise OverflowError('Too Many')
		self.year = year
	def getYear(self):
		return self.year
	def say(self,toWhom,something):
		return Mitperson.say(self.toWhom,'excuse me , but ' + something)


#It is also inherit from mitperson class
class Prof(Mitperson):
	def __init__(self,familyName,firstName,rank):
		Mitperson.__init__(self,familyName,firstName)
		self.rank=rank
		self.teaching={}
	def addTeaching(self,term,subj):
		try:
			self.teaching[term].append[subj]
		except KeyError:
			self.teaching[term]= [subj]
	def getTeaching(self,term):
		try:
			return self.teaching[term]
		except KeyError:
			return None
	def lecture(self,toWhom,something):
		return Mitperson.say(toWhom,something + 'it is something')
	def say(self,toWhom,something):
		if type(toWhom) == UG:
			return Mitperson.say(self.toWhom, ' i don not understand why you say ' + something )
		elif type(toWhom) == Prof:
			return Mitperson.say(self.toWhom, ' i reall y liked your papper ' + something)
		else:
			return self.lecture(toWhom,something)

				
			

class Faculty(object):
	def __init__(self):
		self.names=[]
		self.IDs= []
		self.members=[]
		self.place =None
	def add(self,who):
		if type(who) != Prof:raise TypeError('not a professor')
		if who.getIdNum() in self.IDs:raise ValueError("Duplicate id")
		self.names.append(who.familyName())
		self.IDs.append(who.getIdNum())
		self.members.append(who)
	# whenever you want for loop in your class then you need two method
	#1. __iter__,2. next like this way
	def __iter_(self):
		self.place =0
		return self
	def next(self):
		if self.place >= len(self.names):
			raise StopIteration
		self.place +=1
		return self.members(self.place -1)




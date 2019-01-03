class Human:
	def __init__(self, age):
		self.age = age
		print ("I\'m human")
	def talk(self, message):
		print(message)
class Engineer(Human):
	def __init__(self):
		print("Hello")
	def program(self,language):
		print("I\'m going to program in:", language)
class Lawyer(Human):
	def __init__(self,college,args):
		#print(args)
		super(Human).__init__(type(args))
		print ("Lawyer from the", college)
	def studyCase(self,about):
		print ("I\'m going to study the case of", about)
#Altered order, brings altered init functions priorities
class Student(Lawyer, Engineer):
	pass
Luke = Student("UTN", 28)
print(Luke.age)
Luke.talk("Hello")
Luke.program("Java")
Luke.studyCase("Marriage")
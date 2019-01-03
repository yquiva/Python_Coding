__author__ = 'YQV' #
print ("This program get any age you enter and determine the age range of a person\n")
#opt stands for options, which is goind to be choose by the user:
opt = str(input("Do you want to check an age? Write \'Y\' for yes or anything else for no: "))
if opt == "Y" or opt == "y" :
	while opt == "Y" or opt == "y" :
		try :
			age = int(input("Write your age: "))
			if age < 0 :
				print ("You have not been borned yet")
			elif 0 >= age < 18 :
				print ("You are underage")
			elif 18 >= age < 27 :
				print ("You are a teenager")
			elif 28 >= age < 58 :
				print ("You are an adult")
			else :
				print ("You are elderly old")
			#
			opt = input("Would you like to check another age? Write \'Y\' for yes: ")
		#if user types 
		except :
			opt = input("That is not a number. Would you like to check another age? Write \'Y\' for yes or anything else for no: ")
else :
	print ("Thanks for using the program.")
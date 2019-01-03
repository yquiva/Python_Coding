#General information about the program for the user
print ("This program will help you translate grades from numeric values to its equivalents on the school grading system.")
print ("Grading system: grades go from 1 to 100, but gives to the students the grade in letters and not in numbers. A = from 91 to 100, B = from 71 to 90, C = from 61 to 70, D = from 50 to 69 and E = from 1 to 49.")
#Import library to use decimal, to round numbers to 2 decimals.
#from decimal Import Decimal
#Create variable continuewhile with user input. 
continuewhile = int(input("Would you like to translate any grade? Type 1 for yes, 0 (or any other number except 1) for no: "))
while continuewhile == 1 :
	#Use try to make sure the input is a number. Otherwise with except it will send a message. 
	try :
		grade = round((float(input("Please enter the grade (in numbers) that you will like to translate (if more than 2 decimal are used, the number will be rounded to 2 decimal by the system): "))),2)
	except :
		print ("However, the value enter is not a number. Please type a number from 1 to 100 in numbers.")
	#Continue with the normal flow if a number was ingress on variable grade. 
	else :
		print ("The grade provide is: " ,grade, ".")
		if 1.00 <= grade <= 100.00 :
			if  1.00 <= grade <= 49.99 :
				print (grade, " translates to E on the school grading system.")
				grade = 5
			else :
				if 50.00 <= grade <= 60.99 :
					print (grade, " translates to D on the school grading system.")
					grade = 4
				else :
					if 61.00 <= grade <= 70.99 :
						print (grade, " translates to C on the school grading system.")
						grade = 3
					else :
						if 71.00 <= grade <= 90.99 :
							print (grade, " translates to B on the school grading system.")
							grade = 2
						else :							
							print (grade, " translates to A on the school grading system.")
							grade = 1
			if grade == 1 or grade == 2 :
				print ("This means the student pass.")
			else : 
				print ("This means the student did not pass.") 
		else :
			print ("However, " ,grade, " is not a valid value. Please type a number between 1 and 100.")
	continuewhile = int(input("Would you like to translate another grade? Please type 1 for yes, 0 (or any other number except 1) for no: "))
print ("Thank you for using this program.")
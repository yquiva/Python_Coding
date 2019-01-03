age = int(input ("Write your age: "))
while  age <= 31 :
	#15 will be skipped
	if (age == 15) :
		age += 1
		continue
	if (age == 31) :
#The process in the loop will end
		break
	print ("You have: " + str(age))
	age += 1
#Set the author of the code 
__author__ = "YQV"
#Using the return on a function
def my_function(num1, num2) :
	return (num1 + num2)
#Save result in a variable result_of_Sum
result_of_Sum = my_function(3,4)
print (result_of_Sum)
#Same Example, but asking the user the numbers:
num1 = int(input("Please write the first number: "))
num2 = int(input("PLease write the second number: "))
result_of_Sum = my_function(num1,num2) 
print (result_of_Sum)
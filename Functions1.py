#Set the author of the coding
__author__ = "YQV"
#"def" is a reserve word in Python that means "define".
def my_function(num1=0,num2=0) :
	print (num1 + num2)
#After declare my function, I need to execute it:
#Values will be zero
print ("Result of the function without changing the variables:")
my_function()
#The 'num1' will become 3
print ("Result of the function without changing the first variable to 3:")
my_function(3)
#The "num1" will become 3 and the num2 will become 4
print ("Result of the function without changing the variables to 3 and 4:")
my_function(3,4)
#Same example, but asking the user the numbers:
print ("Please enter the two numbers that you would like to sum.")
num1 = int(input("Write the first number: "))
num2 = int(input("Write the second number: "))
my_function(num1, num2)
#Execute in terminal

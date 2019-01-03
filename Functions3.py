#Set the author of the code
__author__ = "YQV"
#Defining the function: ("somethingMore" will become a "Dictionary", so we print accordingly to its keywords)
def my_function(cad, v=2, **somethingMore) :
	print(cad*v)
	print(somethingMore['extraString'])
	print (somethingMore['anotherString'])
#Activation of the Function and assignation of Dictionary's keyword: (in this case, 'extraString' is the keyword of the first value of the dictionary)
my_function("Python ", 5, extraString = "\nHello", anotherString = "\nBye")
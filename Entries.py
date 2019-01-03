#The input NEEDS to be "saved" on a variable, because is a data that the user inputs from the keyboard.
valor = input()
#All value that comes from the user's keyboard is automatically consider as a string by Python
print (type(valor))
#We print it as any other string
print (valor)
#To make it an integer, we should firstly ask for a number, make sure the user will write a number, and then cast the variable into a integer type
valor = int(valor)
#The value changes to integer
print (type(valor))
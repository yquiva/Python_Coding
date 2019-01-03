#To avoid values issues when expecting an integer and receiving a letter, we just create a try-catch exception
try:
	valor = input("Write a Number: ")
	valor = int(valor)
except:
	print ("That isn't a number")
else:
	print (valor)
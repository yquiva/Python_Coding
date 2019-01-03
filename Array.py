print ('Part 1')
#Declare the Array list
l = [2,"tres",True,["uno",10],5,'Hi']
print (l)
#Using the Array Index
l2 = l[1]
print (l2)
print (str(l[0]))
print (str(l[3]))
#Accessing Array's index that are in an Array list: [indexlnArray][indexlnList]
l3 = l[3][0]
print (l3)
print (str(l[3][1]))


print ('\nPart 2')
#PART II
#Modify inner array's data with the index:
#Ind 0,    1,     2,  [   3    ], 4,  5
l = [2, "tres", True, ["uno",10], 5, 'Hi']
print ('Imprimir lista:', l)
l[1] = 4
l2 = l[1]
print ('Imprimir cambio de dato en indice uno:', l2)
#Slicing: Copy some information from an Array towards another one [begginingIndex:QuantityOfCopyingElements]:
l3 = l[0:3]
l7 = l[1:2]
print ('Imprimir slicing de indice 0, 3 elementos:', l3)
print ('Imprimir slicing de indice 1, 2 elementos:', l7)
#Copy some information from an Array towards another one by skipping some information [beginningIndex:QuantityOfCopyingElements:AmountOfSkipsPerIndex]
l4 = l[0:3:2]
print ('Imprimir desde indice 0, 3 elementos, saltando cada 2 elementos:', l4)
#Copy some information from an Array towards another one by skipping each we want [begginginIndex::AmountOfSkipsPerIndex]
l5 = [2, "tres",True,["uno",10],6]
l6 = l5[0::2]
print ('Imprimir lista 5:', l5)
print ('Imprimir la informacion saltando los datos consecutivos:', l6)


 
print ('\nPart 3')
#PART 3
#Changing several elements in the Array-List [FromIndex:QuantityOfElements]:
l5 = [2, "tres", True,["uno", 10], 6]
print ('Original l5', l5)
l5[0:2] = [4, 3]
print ('New l5 after modification:', l5)
#Modify several elements in the Array-List with just one data [FromIndex:QuantityOfElements]:
l6 = [2, "tres", True, ["uno", 10], 6]
print ('Original l6:', l6)
l6[0:2] = [5]
print ('L6 after modification:', l6)
#Get data from an array with negative index:
l6 = [2, "tres", True, ["uno", 10], 6]
print ('New l6:', l6)
l7 = l6[-1]
l8 = l6[-2]
print ('l7 (-1 index from l6): ', l7)
print ('l8 (-2 index from l6): ', l8)
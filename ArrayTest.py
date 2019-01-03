"""- Create an array list in Python that had:
one integer number, 
one double quotation string, 
one Boolean, 
another array inside with at least 3 elements of your choice on it, 
a float number, 
and a single quotation string; 
the order could vary as however you like it, but all elements should be present. (8pts)
- The array name will be “readyList1”. You should print it. (2pts)"""

#Creating array readyList1
readyList1 = [1, "\"double-quotation string\"", True, [3.0, 3.1, 3.2], 4.0, '\'single-quotation string\'']

#Print array readyList1
print ('readyList1: ', readyList1)

"""Afterwards, you need to change the third index of that array, into a number 5, and 
re-printing the array with the new data on the third index. (3pts)"""
#Replacing index 2 from readyList1 with a '5'
readyList1[2] = 5

#Printing new readyList1
print ('\nNew readyList1 after replacing third index (index 2) of the array with number 5: ', readyList1)

"""- You will make some “slicing” beginning from index 1 and copying 3 elements on the array readyList1, 
by doing it on the readyList2 variable. Then print both lists (5pts)"""
#Creating readyList2 with 3 elements from readyList1, starting on index 1
readyList2 = [readyList1[1:4]]

#Print readyList2
print ('\nreadyList2 (including 3 elements from readyList1 starting from index 1): ', readyList2)

#Print readyList1
print ('\nreadList1 (reprinting it as requested by the exercise): ', readyList1)

"""By creating a readyList3 variable, you will fill it with the same information on the original 
readyList1 and print it. (10pts)"""

#Creating array readyList3
readyList3 = [1, "\"double-quotation string\"", True, [3.0, 3.1, 3.2], 4.0, '\'single-quotation string\'']

#Print array readyList3
print ('\nreadyList3 (which includes the same elements as the original readyList1 array): ', readyList3)

"""With a readyList4 variable, you will fill it from readyList3 variable; by copying the information on it 
from index 0, but skipping every two elements. (3pts)"""
#Creating readyList4
readyList4 = [readyList3[0::2]]

#Printing readyList4 (this was not included on the steps of the test, but it helps demostrate readyList4 accomplish what was required)
print ('\nreadyList4 (which includes elements from readyList3, starting from index 0 but skipping every two elements): ', readyList4)
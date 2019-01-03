"""Create an array list in Python that had one integer number, one double quotation string, one Boolean, 
another array inside with at least 5 elements of your choice on it, a float number, and a single quotation 
string; the order could vary as however you like it, but all elements should be present"""
"""The array name will be “arrayList1”. You should print it."""
arrayList1 = [0, "\"double-quote string\"", True, [3.0,3.1,3.2,3.3,3.4], 4.0, '\'single-quote string\'']
print ('Original arrayList1: ', arrayList1)
"""Afterwards, you need to change the index 3 of that array, into a number 10, and re-printing the array 
with the new data on the index 3."""
arrayList1[3] = 10
print ('\nNew arrayList1 after replacing index 3 with value 10: ', arrayList1)
"""You will make some “slicing” beginning from the second index and copying 4 elements on the array arrayList1, 
by doing it on the arrayList2 variable. Then print both lists."""
arrayList2 = arrayList1[1:5]
print ('\nPrinting new arrayList1 again, as requested by the exercise: ', arrayList1)
print ('\narrayList2 (which is a slicing from arrayList1 beginning with the second index (index 1) and copying 4 elements): ', arrayList2)
"""By creating a arrayList3 variable, you will fill it with the same information on the original arrayList1 
and print it."""
arrayList3 = [0, "\"double-quote string\"", True, [3.0,3.1,3.2,3.3,3.4], 4.0, '\'single-quote string\'']
print ('\narrayList3 (which includes the same elements as the original arrayList1):', arrayList3)
"""With an arrayList4 variable, you will fill it from arrayList3 variable; by copying the information on it from 
the first index, zero, but skipping every two elements."""
arrayList4 = arrayList3[0::2]
print ('\narrayList4 (which includes the elements from arrayList3 starting from index 0, but skipping every two elements): ', arrayList4)
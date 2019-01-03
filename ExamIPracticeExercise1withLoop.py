print ("This program will determine the price to pay after a purchase on the store.")
print ("List of products cost: products class A cost $750; products class B cost $1500, products class C cost $500, and products class D cost $250.")
print ("Current offers: Products class A with a 75\% discount and products class B with a 25\% discount.")
continuewhile = int(input("Would you like to make a purchase? Please choose 1 for yes, 0 (or any other number except 1) for no: "))
while continuewhile == 1:
	try:
	    quantityA = int(input("Please enter the amount of A class objects purchased: "))
	    quantityB = int(input("Please enter the amount of B class objects purchased: "))
	    quantityC = int(input("Please enter the amount of C class objects purchased: "))
	    quantityD = int(input("Please enter the amount of D class objects purchased: "))
	except:
	    print ("That isn't a number")
	else:
	    print ("Quantity of products by class ingressed: Class A: " ,quantityA, ", class B: " ,quantityB, ", class C: " ,quantityC, ", and class D: " ,quantityD, ".")
	if quantityA < 0 or quantityB < 0 or quantityC < 0 or quantityD < 0:
	    print ("However, one or more of the values ingressed are negative, and that is not an option. No calculation will be done")
	else:
	    if quantityA == 0 and quantityB == 0 and quantityC == 0 and quantityD == 0:
	            print ("However, all the values ingress are zero, meaning there is no purchase. The program will end now without making any calculation.")
	    else:
	        fullpriceA = quantityA * 750
	        discountA = fullpriceA * 0.75
	        finalpriceA = fullpriceA - discountA
	        fullpriceB = quantityB * 1500
	        discountB = fullpriceB * 0.25
	        finalpriceB = fullpriceB - discountB
	        finalpriceC = quantityC * 500
	        finalpriceD = quantityD * 250
	        totaldiscount = discountA + discountB
	        totalamount = finalpriceA + finalpriceB + finalpriceC + finalpriceD 
	        print ("Details of amounts to pay: Original Price of Products class A: ", fullpriceA, "$, price of products class A with discount: " ,finalpriceA, "$, you are saving: " ,discountA, "$. Original Price of Products class B: ", fullpriceB, "$, price of products class B with discount: " ,finalpriceB, "$, you are saving: " ,discountB, "$. Price of products class C: " ,finalpriceC, "$. Price of products class D: " ,finalpriceD, "$. Total amount to pay: "  ,totalamount, "$. You saved: " ,totaldiscount, "$.")
	continuewhile = int(input("Would you like to change the quantity of items purchased? Please enter 1 for yes, 0 (or any other number except 1) for no: "))
print ("Thanks for using this program.")
print ("This program will provide the final amount to pay depending of your purchase.")
print ("Our prices: Products A cost $1000, products B cost $500, products C cost $250, products D cost $100, and products E cost $50.")
print ("Our current offers: Products A with a 75% discount, products B with a 50% discount, and products C with a 25% discount.")
continuewhile = int(input("Would you like to buy something? Please type 1 for yes, 0 (or any other number except 1) for no: "))
while continuewhile == 1:
	try:
		quantityA = int(input("How many products A would you like to buy? (please enter a number, if you type letters, the information will not be recognized): "))
		quantityB = int(input("How many products B would you like to buy? (please enter a number, if you type letters, the information will not be recognized): "))
		quantityC = int(input("How many products C would you like to buy? (please enter a number, if you type letters, the information will not be recognized): "))
		quantityD = int(input("How many products D would you like to buy? (please enter a number, if you type letters, the information will not be recognized): "))
		quantityE = int(input("How many products E would you like to buy? (please enter a number, if you type letters, the information will not be recognized): "))
	except :
		print ("That is not a number")
	else:
		print ("These are the quantity of objects requested. Class A: " ,quantityA, ". Class B: " ,quantityB, ". Class C: " ,quantityC, ". Class D: " ,quantityD, ", and Class E: " ,quantityE, ".")
		if quantityA / 1 == quantityA and quantityB / 1 == quantityB and quantityC / 1 == quantityC and quantityD / 1 == quantityD and quantityE / 1 == quantityE:
			if quantityA < 0 or quantityB < 0 or quantityC < 0 or quantityD < 0 or quantityD < 0 :
				print ("However, one or more of the values provided are negative, and those are not valid values. Therefore, no calculations will be done with those.")
			else :
				if quantityA == 0 and quantityB == 0 and quantityC == 0 and quantityD == 0 and quantityE == 0 :
					print ("However, all the values ingressed are zero, meaning there is no purchase. Therefore, no calculations will be done.")
				else :
					regularpriceA = quantityA*1000
					discountA = regularpriceA*0.75
					finalpriceA = regularpriceA-discountA
					regularpriceB = quantityB*500
					discountB = regularpriceB*0.50
					finalpriceB = regularpriceB-discountB
					regularpriceC = quantityC*250
					discountC = regularpriceC*0.25
					finalpriceC = regularpriceC-discountC
					finalpriceD <- quantityD*100
					finalpriceE <- quantityE*50
					finalprice <- finalpriceA+finalpriceB+finalpriceC+finalpriceD+finalpriceE
					finaldiscount <- discountA+discountB+discountC
					print ("These are the details of your purchase. The regular price for products A is: $" ,regularpriceA, ", applying the discount, the new price is: $" ,finalpriceA, ", you are saving: $" ,discountA, ". The regular price for products B is: $" ,regularpriceB, ", applying the discount, the new price is: $" ,finalpriceB, ", you are saving: $" ,discountB, ". The regular price for products C is: $" ,regularpriceC, ", applying the discount, the new price is: $" ,finalpriceC, ", you are saving: $" ,discountC, ". The price for products D is: $" ,finalpriceD, ". The price for products E is: $" ,finalpriceE, ". Your total amount is: $" ,finalprice, ". You are saving: $" ,finaldiscount, ".")
		else :
			print ("However, one or more of the values ingressed are not numbers, and those are not valid values. Therefore, no calculations will be done with those.")
		continuewhile = int(input("Would you like to keep purchasing? Please enter 1 for yes, 0 (or any other number except 1) for no: "))
print ("Thanks for using this program")
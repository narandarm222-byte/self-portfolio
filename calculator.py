def add(num1,num2):
	return num1 + num2
def subt(num1,num2):
	return num1 - num2
def mult(num1,num2):
	return num1 * num2
def div(num1,num2):
	return num1 / num2
def exp(num1,num2):
	return num1 ** num2
def root(num1,num2):
	if num1 < 0:
		return -(-num1 ** (1/num2)) 
	else:
		return num1 ** (1/num2)
	
run = True
while run:
	try:
		num1 = float(input("Enter 1st number "))
		num2 = float(input("Enter 2nd number "))
		op = int(input("Choose the operation | 1(addition), 2(subtraction), 3(multiplication), 4(division), 5(exponention), 6(root) "))
	
		if op == 1:
			print(add(num1,num2))
		elif op == 2:
			print(subt(num1,num2))
		elif op == 3:
			print(mult(num1,num2))
		elif op == 4:
			if num2 == 0:
				print("It's impossible to divide any number to 0 ")
			else:
				print(div(num1,num2))
		elif op == 5:
			print(exp(num1,num2))
		elif op == 6:
			if num2 % 2 == 0 and num1 < 0:
				print("Impossible")
			else:
				print(root(num1,num2))
		else:
			print("Choose one of the options")
		
		act = input("Would you like to do calculation again | if YES type (y) / else any letter ")
	
		if act.lower() == "y":
			continue
		else:
			run = False
	except:
        print("Invalid input! Please enter numbers only and select a valid operation.")

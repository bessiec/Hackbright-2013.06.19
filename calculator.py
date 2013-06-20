def add(num1, num2):
    sum = num1 + num2
    return sum

def subtract(num1, num2):
	difference = num1 - num2
	return difference

def multiply(num1, num2):
	product = num1 * num2
	return product

def divide(num1, num2):
    quotient = float(num1 / num2)
    return quotient

def square(num1):
    squared_number = num1 * num1
    return squared_number

def cube(num1):
    cubed_num = num1 ** 3
    return cubed_num

def power(num1, num2):
    exponents = num1**num2
    return exponents
def mod(num1, num2):
    mod = num1 % num2
    return mod




while True:
#repeat forever
	#read input
	print "calculate away!"
	input = raw_input("> ")
	#tokenize input
	tokens = input.split(" ")
	#if first token is "q", quit
	if tokens[0] == "q":
		break
	elif tokens[0] == "+":
		print add(int(tokens[1]),int(tokens[2]))
	elif tokens[0] == "-":
		print subtract(int(tokens[1]),int(tokens[2]))
	elif tokens[0] == "*":
		print multiply(int(tokens[1]),int(tokens[2]))
	elif tokens[0] == "/":
		print divide(int(tokens[1]),int(tokens[2]))
	elif tokens[0] == "square":
		print square(int(tokens[1]))
	elif tokens[0] == "cube":
		print cube (int(tokens[1]))
	elif tokens[0] == "pow":
		print power (int(tokens[1]),int(tokens[2]))
	elif tokens[0] == "mod":
		print mod(int(tokens[1]),int(tokens[2]))
	else: 
		print "Try again."
	#otherwise decide which math functions to call 
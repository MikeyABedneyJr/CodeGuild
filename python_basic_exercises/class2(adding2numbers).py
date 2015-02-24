def add(a, b):
	c = a + b
	print("The sum of your numbers is: %i!" % c)


number_1 = raw_input("Give me your number: ")
numInt1 = int(number_1)

number_2 = raw_input("Give me a second number: ")
numInt2 = int(number_2)

add(numInt1, numInt2)
usernum = raw_input("Pick any number you want: ")

try:
	val = int(usernum)
except ValueError:
	print("That's not a number!")
	

if int(usernum) % 2 == 0:
	print "Your number is even!"

else:
	print "Your number is odd!"
# Create a class called customer that takes the customer
# name as a variable and is intialized with age, location
# # of Washington & a credit score of 718.
# Create an object from your customer class with the name of Jessie
# Print the name value of your object
# Change the credit score of your object
# Print the new credit score of your object

class customer():
	def __init__(self, name, age, location, credit_score):
		self.name = name
		self.age = age
		self.location = location
		self.credit_score = credit_score

cust_jessie = customer("Jessie", 37, "Washington", 718)

print "Name: %s  |  Age: %d  |  Location: %s  |  Credit Score: %d" % (cust_jessie.name, cust_jessie.age, cust_jessie.location, cust_jessie.credit_score)
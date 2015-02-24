pet = ['fluffy', 'k9']
pet[0] = "dog"

#if two words it would be 'camel case' which means second word starts with captial
#letter.....example PetGood

class Pet():   #Chris is reading from a blog to explain this....
	def __init__(self, name, species):		#expecting something that is the name and something that is the species
		self.name = name		#common problem is to forget self.whatever
		self.species = species

polly = Pet("Polly", "Parrot")
kit = Pet('Kitty', 'Cat')
print polly.name		#would show Polly
print polly.species		#would print Parrot
print polly.name		#would print Kitty

kit.name = 'The kitteh'  #


--------------------------
class Pet(object):

	def __init__(self, name, species)
			def __init__(self, name, species):
							#method is just a function side a class.
			def ___str__(self):
				return "%s is a %s" % (self.name, self.species)

polly = Pet("Polly", "Parrot")

print polly


#Make a program that you interface with---uses classes--and creates something you can manipulate
#Create a class, then create functions that manipulate that class
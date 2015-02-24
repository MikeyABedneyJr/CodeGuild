phone_book = {'Frodo': {'Name' : 'Frodo', 'Number' : '919-999-1111'},
				'Samwise': {'Name' : 'Samwise', 'Number' : '818-888-2222'}
			}
def current_entries():
	print "-"*75
	print "-"*75
	print "Current phone book entries:\n"
	for i in phone_book:
		for j in phone_book[i]:
			print(phone_book[i][j])
	print "-"*75

run = True

while run:
	print "-"*75
	print "1. Look someone up\n2. Add new entry\n3. Modify entry\n4. Remove an entry\n5. View the directory\n9. Exit this AMAZING program"
	print "-"*75
	print "-"*75
	choice = raw_input("What do you want to do?: ")
	if (choice == "1"):
		print "You've chosen to look someone up..."
		Who = raw_input("Who do you want to look up?: ")
		print "You wanted to look up:"
		print phone_book[Who]['Name']
		print "Whose number is:"
		print phone_book[Who]['Number']
		current_entries()

	if (choice == "2"):
		print "You've chosen to add an entry..."
		AddUserName = raw_input("What is the name of your new entry?: ")
		AddUserNum = raw_input("What is this person's phone number?: ")
		phone_book.update({AddUserName: {'Name' : AddUserName, 'Number' : AddUserNum}})
		current_entries()

	if (choice == "3"):
		print "You've chosen to modify an entry..."
		NameMod = raw_input("Who do you want to change?: ")
		ChangeWhat = raw_input("Type 1 to change the name & 2 to change the number: ")
		
		if (ChangeWhat == "1"):
			print "You've chosen to change the name..."
			ChangeName = raw_input("What is the new name?: ")
			phone_book[NameMod]['Name'] = ChangeName
			current_entries()

		else:
			print "You've chosen to change the number..."
			ChangeNum = raw_input("What is the new number?: ")
			phone_book[NameMod]['Number'] = ChangeNum
			current_entries()

	if (choice == "4"):
		print "You've chosen to remove an entry..."
		NameToRemove = raw_input("Who do you want to remove?: ")
		del phone_book[NameToRemove]
		print "Your phonebook is now: "
		current_entries()

	if (choice == "5"):
		current_entries()

	if (choice =="9"):
		print "I know...I know...this is a pretty epic phonebook :)\n\n"
		run = False


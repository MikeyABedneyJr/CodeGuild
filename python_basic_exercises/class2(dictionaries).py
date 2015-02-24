dictionary = {'name':'Mikey', 'phone_number': '867-5309'} #python orders in most memory efficient manner so phone # might appear first
print dictionary['name']
dictionary['name'] = 'Mykee' #changed value of name
print dictionary['name']
dictionary['age'] = 32
print dictionary #just added a key named "age" which is 32 {'age': 32, 'name': 'Mykee'}


dictionary = {'Chantel': {'name' : 'Chantel', 'phone': 'you wish'}}
print dictionary['Chantel']['phone']  #pulls Chantel key, then accesses 2nd dictionary for phone info
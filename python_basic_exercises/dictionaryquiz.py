# Create a dictionary called people that has another dictionary for each:
# Bob (age 22), Carol (age 47), and Justin (age 14) with their name and age.

people = {"p1": {"name": "Bob", "age": "22"}, "p2": {"name": "Carol", "age": "47"}, "p3": {"name": "Justin", "age": "14"}}
print people["p1"]["name"]

for index, person in people.items():
		print person["name"], person["age"]
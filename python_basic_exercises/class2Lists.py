fruit = ['apple', 'orange', 'grapes', 'blueberries']

print fruit
print fruit[-1]
fruit[3] = "blackberries"

popped_item = fruit.pop([1]) #Can catch popped item to move elsewhere

fruit.insert([BANANAS, 2])

practiceTuple = ([1, 2, 3], ["a", "b", "c"])

print practiceTuple
print practiceTuple[0][1]  #this would call list [1,2,3] the select position 1 (which is 2)
practiceTuple[0][1] = [6]
print practiceTuple[0][1]  #if I did line 15 right, I replaced the number 2 with the number 6

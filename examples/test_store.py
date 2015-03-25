from store import *

# TEST
amazon = Store()

amazon.available_items = {
    111: InventoryItem("Farenheit 451", 10, 4.99),
    222: InventoryItem("World According to Garp", 5, 4.99),
    333: InventoryItem("Stranger in a Stange Land.", 1, 4.99),
}

amazon.customer_list = {
    11: Customer("Bob"),
    22: Customer("Carol"),
}
amazon.customer_list[33] = Customer("Kevin")

# ##
# TEST
# ##

# who are you? select a customer.
bob = amazon.customer_list[11]

# what do you want to buy?
item = amazon.available_items[333]

#how many?
qty = 2

#add to cart
bob.cart.selected_items.append(CartLineItem(item, qty))

#what do you want to buy?
item = amazon.available_items[222]

#how many?
qty = 3

#add to cart
bob.cart.selected_items.append(CartLineItem(item, qty))

#add more? if no then checkout and print cart
print bob.cart

print amazon.find("n")
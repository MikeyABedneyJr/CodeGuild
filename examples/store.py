class Store():
    def __init__(self):
        self.available_items = {}
        self.customer_list = {}
    def find(self,text):
        found_list = []
        for index, item in self.available_items.items():
            name = item.name
            position = name.find(text)
            if position <> -1:
                found_list.append(item)
        return found_list

class InventoryItem():
    def __init__(self, name, on_hand, price):
        self.name = name
        self.on_hand = on_hand
        self.price = price

    def __repr__(self):
        output = ""
        output = output + self.name
        output = output + " @ " + str(self.price)
        return output


class CartLineItem():
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

    def __repr__(self):
        output = ""
        output = output + str(self.quantity)
        output = output + " x "
        output = output + str(self.item)
        output = output + " is "
        output = output + str(self.quantity * self.item.price)
        return output


class Cart():
    def __init__(self):
        self.selected_items = []

    def get_total(self):
        total = 0.0
        for line in self.selected_items:
            line_total = line.quantity * line.item.price
            total = total + line_total
        return total

    def __repr__(self):
        output = "Cart:\n"
        for line in self.selected_items:
            output = output + str(line) + "\n"
        output = output + "\nTotal: " + str(self.get_total())
        return output


class Customer():
    def __init__(self, name):
        self.name = name
        self.cart = Cart()

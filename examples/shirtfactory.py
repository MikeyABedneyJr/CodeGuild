class Shirt():
    def __init__(self, color, size):
        self.color = color
        self.size = size
    def __repr__(self):
        return "{color:'"+ self.color + "',size: '" + self.size+"'}"


class ShirtFactory():
    sizes = ("S", "M", "L", "XL")
    colors = ("red", "green", "blue")

    def makeAllCombos(self):
        shirt_list = []
        for c in self.colors:
            for s in self.sizes:
                shirt_list.append(Shirt(c, s))
        return shirt_list
my_factory = ShirtFactory()
my_shirts = my_factory.makeAllCombos()
print len(my_shirts), my_shirts
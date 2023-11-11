
class Vehicle:
    def __init__(self, price, name):
        self.price = price
        self.name = name
    def startup(self, name, price):
        return (self.name + " will startup")
bmw = Vehicle("35000", "m3")
print(bmw.startup("25000", "m5"))

class School:
    def __init__(self, name, ranking, location):
        self.name = name
        self.ranking = ranking
        self.location = location
    def educate(self):
        return self.name + " is here to educate!"
    def moving(self):
        return self.location + " is the new location of " + self.name
uva = School("uva", "33", "virginia")
print(uva.educate())
print(uva.moving())


class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def expire(self, name, price):
        return self.name + " has expired! Do not eat it!" + " it's only" + self.price + "dollars!"
cheese = Food("goatcheese", str(0.03))
print(cheese.expire("milk", str(0.04)))

#output:
#m3 will startup
#uva is here to educate
#virginia is the new location of uva
#goatcheese has expired! Do not eat it! it's only 0.03 dollars!

class Animal:
    name = ""
    age = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Predator(Animal):
    def bit(self, victim):
        if(isinstance(victim,Mammal)== True):
            victim.die()
        print(self.name,"have eated",victim.name)
class Tiger(Predator):
    pass
class Mammal(Animal):
    def die(self):
        del self
class Zebra(Mammal):
    pass
Tiger1 = Tiger("Semen", 10)
Zebra1 = Zebra("Masha", 7)
Tiger1.bit(Zebra1)

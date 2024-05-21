class Animal(): 
    def __init__(self, vertebrete) -> None:
        self.age = 0
        self.vertebrete=vertebrete
    def sound(self):
        pass

class Mammal(Animal) :
    def __init__(self, legs) -> None:
        self.legs = legs
        super().__init__(True)

class Dog(Mammal) :
    def sound(self):
        print('woof')
class Cat(Mammal) :
    def sound(self):
        print('meow')

seed_list = [0,1,1,0,1,0,1,0,0,1]
obj_list = []
for seed in seed_list:
    if seed
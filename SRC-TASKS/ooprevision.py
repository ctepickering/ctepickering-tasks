class Animal(): 
    def __init__(self, age, vertebrete) -> None:
        self.age = age
        self.vertebrete=vertebrete
    def sound(self):
        pass

class Mammal(Animal) :
    def __init__(self, legs) -> None:
        self.legs = legs
        super().__init__(True)

class Dog(Mammal) :
    def __init__(self) -> None:
        self.sound = "bark"
        super().__init__(True)

class Cat(Mammal) :
    def __init__(self) -> None:
        self.sound = "meow"
        super().__init__(True)

dog1 = Dog()
print(dog1.sound)
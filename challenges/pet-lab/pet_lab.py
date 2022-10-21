class Pet():
    def __init__(self, owner, name):
        self.owner = owner
        self.name = name
    def __str__(self):
        return f'{self.owner}{self.name}'
    def walk(self):
        print(f'{self.owner} is going for a walk with {self.name}')
        

my_pet = Pet('Tim', 'Dozer')

my_pet.walk()

class Dog(Pet):
    def __init__(self, owner, name):
        super().__init__(owner, name)
        self.price = 20
    def __str___(self):
        return f'my name is: {self.name}'
    def bark(self):
        print(f'woof woof, bark bark')
    def chase_tail(self):
        return f'oh boy oh boy oh boy!'
    def getPrice(self): 
        return f'{self.name} costs {self.price}'

new_dog = Dog("Megan", "Heidi")

print(new_dog.bark())
print(new_dog.getPrice())

class Cat(Pet):
    def __init__(self, owner, name):
        super().__init__(owner, name)
        self.price = 10
    def purr(self):
        return f'{self.name} says: meow, purr, hiss!'
    def clean(self):
        return f'{self.name} is cleaning!'
    def getPrice(self):
        return f'{self.name} cost {self.price}'
    def walk(self):
        print(f'strut strut')

new_cat = Cat("Sebastian", "Izzy")
new_cat.name = "Dizzy"
newest_cat = Cat("TanTan", "Glasgow")

print(new_cat.purr())
print(new_cat.clean())
print(new_cat.getPrice())
print(newest_cat.purr())
print(newest_cat.clean())
print(newest_cat.getPrice())


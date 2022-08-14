class Toy_factory:
    def __init__(self, color, name, material):
        self.color = color
        self.name = name
        self.material = material
    def dance(self):
        print("I am dancing")
    def roll(self):
        print("I am rolling")
    def talk(self):
        print("I am talking")


class Animals(Toy_factory):
    def __init__(self, color, name, material, fluffy):
        super.__init__(color, name, material)
        self.fluffy = fluffy
        #truth or false
    def walk(self):
        print("Walk on paws")
    def fight(self):
        print("Fight!")

class Dog(Animals):
    def talk(self):
        print("Bark!")

class Cat(Animals):
    def talk(self):
        print("Meow")

class Bear(Animals):
    def talk(self):
        print("AARG")


class Dolls(Toy_factory):
    def __init__(self, color, name, material, eye_color, gender):
        super.__init__(color, name, material)
        self.eye_color = eye_color
        self.gender = gender
    def walk(self):
        print("walk on foot")
    def wave(self):
        print("Wave hand")

class Ginna(Dolls):
    def talk(self):
        print("Hi, I'm Ginna")

class Jack(Dolls):
    def talk(self):
        print("Hi, I'm Jack")
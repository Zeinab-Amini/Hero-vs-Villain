class Hero:
    def __init__(self, name):
        self.name = name
        self.smartness = 0
        self.strength = 0
        self.power = 0
        self.fashion = 0
        self.looks = 0
        self.speed = 0
    def get_smartness(self):
        return self.smartness
    def set_smartness(self, smartness):
        self.smartness = smartness

    def get_strength(self):
        return self.strength
    def set_strength(self, strength):
        self.strength = strength

    def get_power(self):
        return self.power
    def set_power(self, power):
        self.power = power

    def get_fashion(self):
        return self.fashion
    def set_fashion(self, fashion):
        self.fashion = fashion

    def get_looks(self):
        return self.looks
    def set_looks(self, looks):
        self.looks = looks

    def get_speed(self):
        return self.speed
    def set_speed(self, speed):
        self.speed = speed

    def over_all_score(self):
        average = (self.speed + self.looks + self.fashion + self.power + self.strength + self.smartness) / 6
        return average


class Villain:
    def __init__(self, name):
        self.name = name
        self.smartness = 0
        self.strength = 0
        self.power = 0
        self.fashion = 0
        self.looks = 0
        self.speed = 0

    def get_smartness(self):
        return self.smartness
    def set_smartness(self, smartness):
        self.smartness = smartness

    def get_strength(self):
        return self.strength
    def set_strength(self, strength):
        self.strength = strength

    def get_power(self):
        return self.power
    def set_power(self, power):
        self.power = power

    def get_fashion(self):
        return self.fashion
    def set_fashion(self, fashion):
        self.fashion = fashion

    def get_looks(self):
        return self.looks
    def set_looks(self, looks):
        self.looks = looks

    def get_speed(self):
        return self.speed
    def set_speed(self, speed):
        self.speed = speed

    def over_all_score(self):
        average = (self.speed + self.looks + self.fashion + self.power + self.strength + self.smartness) / 6
        return average



import random


keep_going = input("If you want to add a character type 'a' if you want them to fight type 'f': ")
if keep_going == 'a':
    keep_going = True
elif keep_going == 'f':
    keep_going = False
else:
    print("What? Type it again")

villain_list = []
hero_list = []

while keep_going == True:
    v_or_h = input("Do you want to enter a villain or a hero? v/h:")
    if v_or_h == 'v':
        name = input("Type their name: ")
        v = Villain(name)
        v.set_smartness(int(input("Your Villain's smartness level out of ten: ")))
        v.set_strength(int(input("Your Villain's strength level out of ten: ")))
        v.set_power(int(input("Your Villain's power level out of ten: ")))
        v.set_fashion(int(input("Your Villain's fashion level out of ten: ")))
        v.set_looks(int(input("Your Villain's looks level out of ten: ")))
        v.set_speed(int(input("Your Villain's speed level out of ten: ")))

        villain_list.append(v)

    elif v_or_h == 'h':
        name = input("Type their name: ")
        h = Hero(name)
        h.set_smartness(int(input("Your Hero's smartness level out of ten: ")))
        h.set_strength(int(input("Your Hero's strength level out of ten: ")))
        h.set_power(int(input("Your Hero's power level out of ten: ")))
        h.set_fashion(int(input("Your Hero's fashion level out of ten: ")))
        h.set_looks(int(input("Your Hero's looks level out of ten: ")))
        h.set_speed(int(input("Your Hero's speed level out of ten: ")))

        hero_list.append(h)

    keep_going = input("If you want to add a character type 'a' if you want them to fight type 'f': ")
    if keep_going == 'a':
        keep_going = True
    elif keep_going == 'f':
        keep_going = False
    else:
        print("What? Type it again")


hero = random.choice(hero_list)
villain = random.choice(villain_list)
print(hero.name + " is fighting with " + villain.name)

if hero.over_all_score()> villain.over_all_score():
    print("Yay!!! " + hero.name + " won!!!")
else:
    print(villain.name + " won :(")

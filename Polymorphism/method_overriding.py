class Animal:

    def __init__(self, name):

        self.name = name

    def eat(self):

        print(self.name,"is eating.")

    def make_sound(self):

        print(self.name, "makes a sound...")

class Lion(Animal):

    def make_sound(self):

      print(self.name, "lets out a roar!")

    def eat(self):

        print(self.name,"maws on raw meat!")

class Elephant(Animal):

    def make_sound(self):

      print(self.name, "trumpets majestically!")

    def eat(self):

        print(self.name,"nibbles on fresh fruits!")

class Monkey(Animal):

    def make_sound(self):

      print(self.name, "quickly chatters!")

    def eat(self):

      print(self.name,"chomps on bananas")

a1 = Animal("An animal")

l1 = Lion("Scar")

e1 = Elephant("Jumbo")

m1 = Monkey("George")

#----------------- printing the outputs

a1.make_sound()
a1.eat()

print("-----------")

l1.make_sound()
l1.eat()

print("-----------")

e1.make_sound()
e1.eat()

print("-----------")

m1.make_sound()
m1.eat()
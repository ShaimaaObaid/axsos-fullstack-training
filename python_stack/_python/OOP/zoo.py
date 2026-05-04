class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 100
        self.happiness = 100

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Health: {self.health}")
        print(f"Happiness: {self.happiness}")
        print("-" * 20)

    def feed(self):
        self.health += 10
        self.happiness += 10


# Lion class
class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.roar_power = 50

    def feed(self):
        super().feed()
        self.happiness += 10  


# Monkey class
class Monkey(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.agility = 80

    def feed(self):
        super().feed()
        self.happiness += 5
        self.health -= 5  


# Bear class
class Bear(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.strength = 90

    def feed(self):
        super().feed()
        self.health += 5  


# Zoo class
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
#just animal
    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
        else:
            print("Invalid object! Only animals allowed.")

    def feed_all(self):
        for animal in self.animals:
            animal.feed()

    def print_all_info(self):
        print("=" * 30)
        print(self.name)
        print("=" * 30)
        for animal in self.animals:
            animal.display_info()


# TEST 

zoo1 = Zoo("Wild Life Zoo")

zoo1.add_animal(Lion("Simba", 5))
zoo1.add_animal(Lion("Nala", 4))
zoo1.add_animal(Monkey("George", 3))
zoo1.add_animal(Bear("Baloo", 7))

zoo1.feed_all()
zoo1.print_all_info()
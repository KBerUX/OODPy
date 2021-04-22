# Petshop

class petshop:
    def __init__(self, name, age, breed, color, size):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color
        self.size = size

    def show(self):
        print(f"My name is: {self.name} and I am {self.age} years old. ")

    def color_breed(self):
        print(f"My color is: {self.color} and I am a {self.size} animal")


class Dog(petshop):
    def speak(self):
        print("bark")


class Cat(petshop):
    def speak(self):
        print("meow")


my_cats = [Cat("Emmie", 2, "Maine Coon mix", "brown-orange",
               "small"), Cat("Ollie", 1, "Short-hair", "Grey", "big")]

my_dogs = [Dog("Ivy", 12, "Labrador mix", "black", "medium"),
           Dog("Graham", 1, "Jack-Russel Mix", "brown", "small")]


my_cats1 = [Cat("Allie", 2, "short-hair", "red", "small")]

my_cats = my_cats + my_cats1


for element in my_cats:
    print(element)

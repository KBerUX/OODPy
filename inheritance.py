# Pet is the upper level 'Parent' class
# anything below it is a child class.
# Child will inherit values from parent class
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what I say")


class Cat(Pet):
    def __init__(self, name, age, color):
       # reference the super class which is the class we inherited from Pet
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(
            f"I am {self.name} and I am {self.age} years old and I am {self.color}")


class Dog(Pet):
    def speak(self):
        print("Bark")


class Fish(Pet):
    pass


p = Pet("Tim", 19)
p.show()
p.speak()

c = Cat("Ollie", 2, "grey")
c.speak()
c.show()


d = Dog("Ivy", 12)
d.show()
d.speak()

f = Fish("Bubbles", 2)
f.speak()
f.show()

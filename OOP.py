

# the string we typed is the object of the class string.
# print(type("hello"))


#string = "hello"
# .upper is a methodand you can pass an argument into. The method upper is
# acting on the object of type String which is stored in string variable
# print(string.upper())


class Dog:
    # method is function that goes inside of a class
    def __init__(self, name, color):
        self.name = name
        self.color = color


dognames = [Dog('Chelsea', 'Amber'), Dog('Domo', 'Green')]

print(dognames[0])

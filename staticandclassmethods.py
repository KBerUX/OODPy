# class attributes are attributes specific to that class
class Person:
    # number of people is a class attribute because it is defined for the
    # entire class it is not specific for an instance.
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    # this method is not specific to an instance. It will be called to the class itself and for
    # this situation, will return the number of people

    @classmethod
    def number_of_people(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person("Tim")
p2 = Person("James")
print(Person.number_of_people_())

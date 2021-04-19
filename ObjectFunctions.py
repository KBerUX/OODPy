# class function modifies objects in the class or give me specific information of those objects

class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

# class function that checks if someone is in honor roll or not.
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

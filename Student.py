# class you can define your own data type
# class is a template and defines Student
# in this instance
class Student:
    # attributes associated with student
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
        # actual object's name is the name passed in.
        # need to take the values passed in and assign
        # them to the objects' values
        # the name of the student class is equal to the object's name
        # in the app that was passed in

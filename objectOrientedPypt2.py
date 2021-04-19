

class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    @property
    def name(self):
        print("getting name")
        return self._name

    @name.setter
    def name(self, name):
        print("setting name")
        self._name = name

    def update_membership(self, new_membership):
        print("Calculating costs")
        self.membership_type = new_membership

    def __str__(self):
        print("converting to string")
        return self.name + " " + self.membership_type

    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True

        return False

    __hash__ = None
    __repr__ = __str__


customers = [Customer("Caleb", "Gold"),
             Customer("Kist", "Plat")]

print(customers[0] == customers[1])
print(customers[0].name)
print(customers)

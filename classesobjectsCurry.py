class Customer:
    def _init_(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
        print("Testing out")


c = Customer("Kist", "Gold")
print(c.name, c.membership_type)

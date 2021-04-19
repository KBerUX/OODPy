# very basic class
class Customer:
    # function defined within a class which is this method def _init_():
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
        print("Customer was created")

# def read_customer():
# is a static method
# bc it is not attached to any individual object
# but is invoked on the class itself
#    def read_customer():
#        print("Reading customer from DB")

# def __str__(self):
# Will invoke anytime when it tries to turn a customer into a string


def _str_(self):
    print("converting into a string")
    return self.name + " " + self.membership_type


def print_all_customers(customers):
    for customer in customers:
        print(customer)


customers = [Customer("Kist", "Gold"),
             Customer("Caleb", "Silver")]


Customer.print_all_customers(customers)


# print(customers[1].name)
# print(customers[1].membership_type)
#customers[1].membership_type = "Platinum"
# print(customers[1].membership_type)
# Customer.read_customer()

print(customers[1])


# attributes provide the data that is stored for the object (customer)
# methods provide functionality
# --> this is a method that already exist
# def _init_(self,): the initializer/constructor

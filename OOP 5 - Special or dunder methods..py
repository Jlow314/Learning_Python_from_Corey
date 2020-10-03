# special methods surrounded by __ = 'Dunder". Example __init__ (implicitly called upon when we create our employee objects)

# __repr__  : gives unambigous representation of the object, meant to be seen by developers debugging
# __str__ : gives a readable representation of the object meant for the userr


class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = round(self.pay * self.raise_amt)

    def __repr__(self):
        return f"Employee({self.first},{self.last},{self.pay})"

    def __str__(self):
        return f"Employee {self.fullname()} - {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


print(len("test"))
# len() also uses a special dunder method in the back
print("test".__len__())
# so suppose we want to run len() on employee object to return the full name's length

emp_1 = Employee("Juan", "Lopez", 90000)
# emp_2 = Employee("Levi", "Lopez", 60000)
print(len(emp_1))


# print(emp_1)
# # implicitly runs print(emp_1.__str__) which automaticallu falls back to print(emp_1.__repr__) is __str__ is not defined

# print(emp_1 + emp_2)
# + uses the __add__ dunder method of the employee object which is defined to add pays.

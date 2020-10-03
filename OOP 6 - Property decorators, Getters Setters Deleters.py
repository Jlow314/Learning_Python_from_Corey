# class Employee:
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = f"{first}.{last}@company.com"

#     def fullname(self):
#         return f"{self.first} {self.last}"


# emp_1 = Employee("Juan", "Lopez", 90000)

# emp_1.first = "Jim"
# print(emp_1)
# print(emp_1.email)
# print(emp_1.fullname())

# property decorators allow our class to give it getter/setter/deleter functionality
# email depends on first and last name
# emp_1.first = "Jim" > fullname is correct, but email is not
# every time we run fullname, it grabs the current first/last name
# email attribute is not changed because __init__ is not reran
# we want to update email when first/last is changed
# > getters - setters in Java. In Python use property decorator
# property decorators allow to define a method, but access it like an attribute

# remove attribute email and put it in method to print it out
# but we do not want to change the code to print(emp_1.email())
# we want to access it still like an attribute:
# add @property
# we define our email like a method, but still continue to access it like an attribute


# class Employee_alt:
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last

#     @property
#     def email(self):
#         return f"{self.first}.{self.last}@company.com"

#     @property
#     def fullname(self):
#         return f"{self.first} {self.last}"


# emp_alt = Employee_alt("Juan", "Lopez", 90000)

# emp_alt.first = "Jim"
# print(emp_alt)
# print(emp_alt.email)
# print(emp_alt.fullname)

# Say we want the ability to do emp_1.fullname = "Juan Lopez"
#  so that it changes the fist, last  and email. that is where we use a SETTER
# the name that we use for our setter, is the  name of oour property:
# @fullname.setter
# and under that decorator, create another method with the same name
# def fullname, with name being the  fullname we pass along


class Employee_alt:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None


emp_alt = Employee_alt("Juan", "Lopez", 90000)
print(emp_alt)
print(emp_alt.email)
print(emp_alt.fullname)

emp_alt.fullname = "Levi Lopez"
print("--------------------------")
print(emp_alt.email)
print(emp_alt.fullname)

del emp_alt.fullname
print(emp_alt.first)
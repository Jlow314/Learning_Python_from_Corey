class Employee:
    pass


emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
# this is an instance variable, not a class variable.
# instance variable contain data which is unique for each instance

emp_1.first = "Corey"
emp_1.last = "Schafer"
emp_1.email = "Corey.Schafer@company.com"
emp_1.pay = 50000

emp_2.first = "Test"
emp_2.last = "User"
emp_2.email = "test.user@company.com"
emp_2.pay = 60000

# each of above instances have attributes which are unique to them

print(emp_1.email)
print(emp_2.email)

# instead of setting first, last etc manually, let's say we
# set these automatically when the employee is created.
# to do this, we use a special init method (=contructor in other languages) which is
# run automatically when calling the class


# now when we create methods in a class, they (receive) the instance as the 1st argument
# this instance by convention we call it 'self'
# other arguments can be defined next.

# each method in a class takes the instance as the first argument


class employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"


# equivalent to emp_1.first = 'Corey'

# now to create a new instance using this class, we can call the class
# and pass the arguments. The self argument is passed automatically as first instance
# and does not need to be declared

emp_3 = employee("Juan", "Lopez", 9000)
print(emp_3.email)

# email, name, age, pay are all attributes of the class.
# if we want to perform an action against the class: add method to a class

# example action is display full name


class employee_with_action:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return self.first + " " + self.last


emp_4 = employee_with_action("Levi", "Lopez", 20000)

print(emp_4.pay)
print(emp_4.fullname())
# it states fullname() instead of fullname because it is a method to run
# without (), it would be an argument

# following are the same:
# emp_4.fullname()    where emp_4 is an instance of the class, passed automaticcally as first argument in the method
# employee_with_action.fullname(emp_4) where the mehod is called upon the class itself, not the class instance - so you need to pass the instance as argument


# these emp_x are instance variables. Next lesson talks about class variables.
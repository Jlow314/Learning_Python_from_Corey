class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"
        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} "{self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


print(Employee.num_of_emps)
emp_1 = Employee("Juan", "Lopez", 90000)
emp_2 = Employee("Levi", "Lopez", 50000)

print(Employee.num_of_emps)

# print(emp_1.__dict__)
# # print(Employee.__dict__)

# emp_1.raise_amount = 1.05
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.raise_amount)

print(emp_1.__dict__)
# print(emp_2.email)

# print(emp_1.raise_amount)
# Employee.apply_raise(emp_1)
# print(emp_1.pay)

# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

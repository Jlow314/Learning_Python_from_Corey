class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # use  of classmethods as alternative class contructors
    @classmethod
    def from_str(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


import datetime

my_date = datetime.date(2020, 10, 3)
print(Employee.is_workday(my_date))


emp_1 = Employee("Juan", "Lopez", 90000)
emp_2 = Employee("Levi", "Lopez", 30000)

# emp_str_1 = "John-Doe-70000"
# emp_str_2 = "Steve-Smith-60000"

# new_emp_1 = Employee.from_str(emp_str_1)
# print(new_emp_1.pay)


# print(new_emp_1.name)

# emp_1.set_raise_amt(1.05)

# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)

# # print(emp_1.__dict__)
# # emp_1.raise_amt = 1.05
# # print(emp_1.__dict__)
# # emp_1.apply_raise()
# # print(emp_1.pay)

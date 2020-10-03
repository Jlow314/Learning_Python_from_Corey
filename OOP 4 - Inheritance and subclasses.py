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


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # super().__init__ is going to pass first/last/pay to Employee's __init__ method and let that class handle that
        # alternative notation : Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        # never pass an empty list or mutable object as default - best practice - hence: None as default and set it with IF
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())


dev_1 = Developer("Juan", "Lopez", 50000, "Python")
dev_2 = Developer("Levi", "Lopez", 30000, "Java")
mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])


print(isinstance(mgr_1, Manager))

print(issubclass(Developer, Employee))

# print(mgr_1.email)
# mgr_1.print_emps()
# print(mgr_1.email)
# mgr_1.add_emp(dev_2)
# mgr_1.print_emps()

# print(dev_1.email)
# print(dev_2.prog_lang)
# print(dev_2.email)
# print(help(Developer))

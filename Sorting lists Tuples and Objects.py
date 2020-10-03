li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

s_li = sorted(li)  # creates a new list to be put in variable

print("Sorted Variable:\t", s_li)
print("Original Variable:\t", li)  # origiinal list remained intact

li.sort()  # changes list in place
print(li.sort())  # return value of the sort method is not a new list
print("Method Sorted variable:\t", li)  # original list has changed

s_li = sorted(li, reverse=True)
print("Reverse sorted variable:\t", s_li)

# we use the sort method when we work on a list, it changes it in place
# sorted function gives more flexibility, as it not only works on lists but
# on any iterable, like tuples:

tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
# tup.sort() a tuple has no sort method

s_tup = sorted(tup)  # will return a sorted list to be put in a variable
print("Tuple\t", s_tup)

# or use sort function on a dictionary
di = {"name": "Corey", "job": "Programming", "age": None, "os": "Windows"}

s_di = sorted(di)  # also returns a list, but only of sorted keys!!
print("Sorted dictionary:\t", s_di)

# sort on different criteria
li2 = [-6, -4, -5, 3, 2, 3, 1]
s_li2 = sorted(li2)
print(s_li2)
s_li3 = sorted(li2, key=abs)
print(s_li3)


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"{self.name},{self.age},{self.salary}"


e1 = Employee("Carl", 37, 70000)
e2 = Employee("Sarah", 29, 80000)
e3 = Employee("John", 43, 90000)
employees = [e1, e2, e3]
print(employees)
# s_employees = sorted(employees)
# will not work, as Python does not know how to sort this list
# it will need a key to sort it on


def e_sort(emp):
    return (
        emp.age
    )  # change this name to age or salary, and below will sort on this acordingly


# sorted() function can take on a key, which is a function. abs = built-in function

s_employees1 = sorted(employees, key=e_sort, reverse=True)
print(s_employees1)


# alternatively, you an import from operator: attrgetter
# this allows to set the key directly without creating a function
from operator import attrgetter

s_employees2 = sorted(employees, key=attrgetter("age"))
print(s_employees2)
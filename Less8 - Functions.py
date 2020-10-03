def Placeholder_func():
    pass


def line():
    print("---------------------------")


line()  # () to execute the function. without, it will be equal to the function itself


def hello_func():
    print("Hello World!")


line()

print(hello_func)  # so without (), so not executing the function
print(hello_func())  # execute the function, and print its return value
hello_func()

line()


def return_function():
    return "This is the return value"


a = return_function()
print(a)
line()
print(len("tekst"))
line()
print(return_function().upper())
line()


def hello_function(greeting):
    return f"{greeting} Function."


print(hello_function("Juan"))
print(hello_function("Juan"))
line()


def hello_function_wih_default(greeting="Hello", name="You"):
    return f"{greeting}, {name}"


print(hello_function_wih_default())
print(hello_function_wih_default(greeting="Hey"))
print(hello_function_wih_default(name="Levi"))
# positional arguments need to come before positional keyword arguments, otherwise you get an error
print(hello_function_wih_default("Yepla"))  # will return an error
# print(hello_function_wih_default(name='Jon','Yepla'))
line()


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


# * and ** as function parameters:
# takes on any arbitrary number of positional arguments or keyword arguments
# the result will create a tuple of all positional arguments taken
# and a dictionary of all keyword arguments (key-value) passed
# on which you can work
student_info("math", "Art", name="Jon", age=22, lastname="Michaels")
#
line()
# we cal also unpack a list, tuple or dictionary and pass this as
# arguments and keyword arguments into a function doing:
courses = ["Math", "Art"]
info = {"name": "Jon", "age": 22, "lastname": "Michaels"}


def function_show_unpacking(*args, **kwargs):
    print(args)
    print(kwargs)


function_show_unpacking(*courses, **info)

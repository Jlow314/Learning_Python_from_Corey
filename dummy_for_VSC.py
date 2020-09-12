import sys

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):

    greeting = "Hello, {}".format(who_to_greet)
    return greeting


Juanoto

r = requests.get("https://www.cisco.com")
print(r.status_code)
# print(r.headers)
print(greet("world"))
# print(greet('Corey'))

name = input("What is your name? ")
print("Hello, ", name)

# in terminal
# cls
# python
# import sys
# sys.executable > pyhton path
# exit()
# within project folder create a venv : python -m venv venv > creates the venv folder. Pick interpreter in venv. Terminal launches witin venv now.
# witin venv : pip install requests
# settings: control space > editor. > all options

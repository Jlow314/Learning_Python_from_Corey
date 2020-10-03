# import my_module as mm
# from the my_module, import all functions and variables defined there.
# to call them, use the (function)method/variable on the abbreviated 'mm'


import sys
import random
import math
import datetime
import calendar
import os
import antigravity

course = ["History", "Math", "Physics", "CompSci"]

# index = my_module.find_index(course, "Math")
# print(index)
# index2 = mm.find_index(course, "Physics")
# print(index2)
# print(mm.test)

print(sys.path)
# first entry in the path is always the directory where we run the script from
# so we can always import modules from the same directory
# next comes the directory defined in the PYTHON path variable
# next come the directories defined through the PYTHONPATH /python.exe which
# make up the standard PYTHON library containing a lot of modules
# last, the site-packages direcotry for 3rd party packages
# to run from the cmd terminal, define the PYTHONPATH environment variable under
# computer > advanced settings > env variable >

from my_module import find_index as fi, test

print(fi(course, "History"))
print(test)


random_course = random.choice(course)
print(random_course)


rads = math.radians(90)
print(rads)
sinus = math.sin(rads)
print(sinus)

vandaag = datetime.date.today()
print(vandaag)

eenszien = calendar.month(2020, 9, 3)
print(eenszien)

print(os.getcwd())

print(os.__file__)

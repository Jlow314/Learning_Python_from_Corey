if True:
    print("Conditional was True")

language = "Python"

if language == "Python":
    print("Conditional was True")

language = "Java"
if language == "Python":
    print("Language is Python")
elif language == "Java":
    print("Language is Java")
elif language == "Javascript":
    print("Language is Javascript")
else:
    print("no Match")

########################
user = "Admin"
logged_in = False

if user == "Admin" and logged_in:
    print("Admin Page")
else:
    print("Wrong credentials")

if not user == "Admin":
    print("you are admin")
else:
    print("you are no admin")

###############################
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)

print(id(a))
print(id(b))

b = a
print(a is b)  # same as stating print(id(a)==id(b))
print(id(a))
print(id(b))
################################
# False values:
# False
# None
# Zero of any numeric type
# any empty sequence. for Example '',[],()
# any empty mapping (= which basically is empty dict). For exampe {}

condition = 0

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")

student = {"name": "John", "age": 25, "courses": ["Art", "Math"]}
print(student)
print(student["name"])

# keys can be anything immutable: integer, lfoat, string. Here str is used
# values can be about anything

# print(student["phone"])
print(student.get("name"))
print(student.get("phone"))
print(student.get("phone", "DOES NOT EXIST"))

student["phone"] = "555 - 5555"
print(student["phone"])
print(student.get("phone", "DOES NOT EXIST"))

student["name"] = "Jane"
print(student)

student.update({"age": 27, "courses": ["Science", "Latin"], "phone": "444-4444"})
print(student)
del student["age"]
print(student)

student.update({"age": 28})
print(student)

age = student.pop("age")
print(age)
print(student)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, value)

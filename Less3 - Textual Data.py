line = "---------------------"
my_message = "Hello's World"
print(my_message)
long_line = """Was a good
long summer
but
now it is gone"""
print(long_line)

message = "Hello World"

print(len(message))
print(message[0])
print(message[10])
# print(message[11])
print(message[:5])
print(message[6:])

print(line)

print(message.upper())
print(message.count("Hello"))
print(message.count("h"))
print(message.count("H"))
print(message.count("o"))
print(message.find("World"))
# print(message.find("world"))

message.replace("World", "Universe")
print(message)
new_message = message.replace("World", "Universe")
print(new_message)
message = message.replace("World", "Universe")
print(message)
print(line)

greeting = "Hello"
name = "Michael"
message = greeting + name
print(message)
message = greeting + ", " + name + ". Welcome!"
print(message)
message = "{}, {}. Welcome!".format(greeting, name)
print(message)

message = f"{greeting}, {name}. Welcome!"
print(message)
message = f"{greeting.upper()}, {name.upper()}. Welcome!"
print(message)
print(line)

print(dir(name))
print(line)
print(help(str))
print(line)
print(help(str.split))

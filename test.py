import sys

# import requests

print(sys.version)
print(sys.path)

# r = requests.get("https://ww.cisco.com")


def greet(who_to_greet):
    greeting = f"Hello {who_to_greet}"
    return greeting


print(greet("Juan"))
# print(r.status_code)a

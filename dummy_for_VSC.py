import requests

r = requests.get("https://www.cisco.com")
print(r.status_code)

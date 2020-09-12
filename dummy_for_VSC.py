import requests

r = requests.get("https://www.cisco.com")
print(r.status_code)

# git: in settings gitbash shell path gezet
# open terminal opens gitbash shell
# hierin gitbash configureren : git config --global user.name "Jlow314" en git config --global user.email "lopez.hernandez.juan@gmail.com"
# git config --list > shows us options and username and email

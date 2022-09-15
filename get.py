import requests

req = requests.get("https://raw.githubusercontent.com/XuantongMa/CMPUT-404-Lab1-F22/main/get.py")

print(req.text)

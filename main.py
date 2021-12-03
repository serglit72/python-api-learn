import requests

requests = requests.get("https://playground.learnqa.ru/api/hello")

print(requests.text)

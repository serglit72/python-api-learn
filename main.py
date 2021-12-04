import requests

request = requests.get("https://playground.learnqa.ru/api/hello")

print(request.text)

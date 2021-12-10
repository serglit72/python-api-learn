import requests

url = "https://playground.learnqa.ru/api/long_redirect"
request = requests.get(url)
final = request.url
print("Redirects = ", len(request.history))
print("URL = "+final)
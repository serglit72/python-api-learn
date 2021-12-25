import requests
import pytest


def test_cookie_print():

    url = "https://playground.learnqa.ru/api/homework_cookie"

    response = requests.get(url)
    cookie = dict(response.cookies)

    print(f"The value for given cookie is {cookie['HomeWork']}")

    assert "HomeWork" in cookie, "No 'HomeWork' in cookies"


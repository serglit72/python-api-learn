import pytest
import requests

class TestAPI:
    names = [("Antree"),("Neo"),("Trininty")]

    @pytest.mark.parametrize('name', names) #decorator for parameters
    def test_hello(self, name):

        url = "https://playground.learnqa.ru/api/hello"
        # name = "Vitatii"
        data = {"name": name}

        # Check status code for the request
        response = requests.get(url, params=data)
        assert response.status_code == 200, f"Status code is not 200, but {response.status_code}"

        # Check if no such field in response json
        response_json = response.json()
        assert "answer" in response_json, "There is no 'answer' in response"

        # Check if wrong response returned
        expected = f"Hello, {name}"
        assert expected == response_json["answer"], f"Wrong response for {response_json('answer')}"

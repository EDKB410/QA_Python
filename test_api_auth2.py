import pytest
import requests


class TestApiAuth:

    def test_api_auth2(self):
        response2 = requests.get(url="https://playground.learnqa.ru/api/user/login")
        print(response2.json())
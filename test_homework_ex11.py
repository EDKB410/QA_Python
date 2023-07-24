import pytest
import requests

class TestHWex11:

    def test_get_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        print(response.cookies)
        home_work_cookie = "hw_value"
        assert home_work_cookie in response.cookies["HomeWork"], "There is no auth cookie in the response"
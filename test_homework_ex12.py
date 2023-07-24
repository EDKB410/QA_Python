import pytest
import requests

class TestHWex11:

    def test_get_header(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        print(response.headers)
        x_secret_homework_header = "Some secret value"
        assert x_secret_homework_header in response.headers["x-secret-homework-header"], "There is no auth header in the response"
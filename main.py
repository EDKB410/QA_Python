import requests

response_hello = requests.get("https://playground.learnqa.ru/api/hello")
print(response_hello.text)

response_get_text = requests.get("https://playground.learnqa.ru/api/get_text")
print(response_get_text.text)
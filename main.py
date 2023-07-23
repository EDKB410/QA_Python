import requests

payload = {"name": "surname"}
response_get_text = requests.get("https://playground.learnqa.ru/api/get_text", params=payload)
print(response_get_text.text)
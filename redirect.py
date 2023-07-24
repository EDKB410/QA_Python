import requests

response_get = requests.get("https://playground.learnqa.ru/api/long_redirect")
for i in response_get.history:
    print (i.url)
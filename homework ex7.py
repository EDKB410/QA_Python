import requests
import json

payload = {"name": "surname"}

responseHead = requests.head(url='https://playground.learnqa.ru/ajax/api/compare_query_type')
print(responseHead.status_code)
print(responseHead.text)

responseGet = requests.get(url='https://playground.learnqa.ru/ajax/api/compare_query_type', params=payload)
print(responseGet.status_code)
print(responseGet.text)

responsePost = requests.request(method='DELETE', url='https://playground.learnqa.ru/ajax/api/compare_query_type', data=payload)
print(responsePost.status_code)
print(responsePost.text)
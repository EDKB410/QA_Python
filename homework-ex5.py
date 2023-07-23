import requests
import json
from homework_json import *

obj = json.loads(json_text)
print(obj['messages'][1]['message'])

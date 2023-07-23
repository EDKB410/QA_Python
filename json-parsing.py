import json

str_jsn_prs_frmt = '{"answer": "Hello"}'
obj = json.loads(str_jsn_prs_frmt)
#print(obj['answer'])

key = "answer"

if key in obj:
    print(obj[key])
else:
    print(f"Is not {key} found")



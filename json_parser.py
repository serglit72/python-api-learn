import json

json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},\
{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
load_json = json.loads(json_text)
print(load_json['messages'][1])

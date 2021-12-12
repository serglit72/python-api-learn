import requests
import time
import json

print("#STEP 1 - create a task")
url = "https://playground.learnqa.ru/ajax/api/longtime_job"
# create a task
request = requests.get(url) # create a task - call method without TOKEN
response = json.loads(request.text) # getting a json object from string
print(request.text)

token = response["token"]
delay = response['seconds']
wrong_token = response["token"]+"123"

print('#STEP2- check status before time')

print(request.status_code)

request2 = requests.get(url, params={'token': wrong_token})
print("Check if we use wrong token response", request2.text)
print("#STEP3 - create a task and wait for N seconds (variable \"delay\") until the task is DONE")

request = requests.get(url) # create a task - call method without TOKEN
response = json.loads(request.text) # getting a json object from string
print(request.text)
token = response["token"]
delay = response['seconds']
time.sleep(delay)
request3 = requests.get(url, params={'token': token})
print("Check if task is ready", request3.text)


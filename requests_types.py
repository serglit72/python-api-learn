import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

# Assignment 7.1
response1 = requests.get(url)
print("requests.get(url) output: ", response1.text)
# OUTPUT: Wrong method provided

response2 = requests.put(url)
print("requests.put(url) output: ", response2.text)
# OUTPUT: Wrong method provided

response3 = requests.post(url)
print("requests.post(url) output: ", response3.text)
# OUTPUT: Wrong method provided

response4 = requests.delete(url)
print("requests.delete(url) output: ", response4.text)
# OUTPUT: Wrong method provided

# Assignment 7.2
response5 = requests.head(url, params={"method":"GET"})
print("requests.head(url) output: ", response5.text)
# OUTPUT: empty

# Assignment 7.3

response6 = requests.get(url, params={"method":"GET"})
print("requests.get(url) output for GET: ", response6.text)
# OUTPUT: {"success":"!"}

response7 = requests.put(url, params={"method":"PUT"})
print("requests.put(url) output for PUT: ", response7.text)
# OUTPUT: Wrong method provided

response8 = requests.post(url, data={"method":"POST"})
print("requests.post(url) output for POST: ", response8.text)
# OUTPUT: Wrong method provided

response9 = requests.delete(url, data={"method":"DELETE"})
print("requests.delete(url) output for DELETE: ", response9.text)
# OUTPUT: {"success":"!"}

# Assignment 7.4
print("Start for- loop")
methods = ['GET', 'POST', 'DELETE', 'PUT']
for metd in methods:
    response = requests.put(url, data={"method": metd})
    print(f"requests.put(url) output for {metd} : ", response.text)

    response = requests.delete(url, data={"method": metd})
    print(f"requests.delete(url) output for {metd} : ", response.text)

    response = requests.post(url, data={"method": metd})
    print(f"requests.post(url) output for {metd} : ", response.text)

    response = requests.get(url, params={"method": metd})
    print(f"requests.get(url) output for {metd}: ", response.text)

    print("*"*20)






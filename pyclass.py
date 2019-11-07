import requests
r = requests.get('http://api.thecatapi.com/')
print(r.status_code)
k1 = []
for message in r.text:
    for k in message:
        k = str(k)
        k1.append(k)
print(k1)





print(r.text)


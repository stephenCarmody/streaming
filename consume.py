import requests
r = requests.get('http://localhost:5000/time',
                 stream=True)

for line in r.iter_lines():
    print('LINE:', line)
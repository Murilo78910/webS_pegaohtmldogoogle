import requests

response = requests.get('https://www.google.com.br/')

print('Status Code: ' , response.status_code)
print('Header: ')
print(response.headers)

print('\n Content: ')
print(response.content)

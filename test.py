import json

cookies = open('./cookies')

dictCookies = json.load(cookies)

print(dictCookies)
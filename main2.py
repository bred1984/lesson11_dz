import json


class pprint:
    @staticmethod
    def print(s:str):
        print(s)

    @staticmethod
    def print_dict(ddd:dict):
        pass
import os
# import json
# pprint.print('as111dc')
#
# str1='''{"cars":[{"model":"audi"},{"model":"bmw"}]}'''
# d=json.loads(str1)
# print(d,type(d))
#
# sttt=json.dumps(d)
# print(sttt,type(sttt))

# if not os.path.isfile('test1.txt'):
#     open('test1.txt','w')
#
# with open('test1.txt','a') as f:
#     f.writelines('sdwc')

import requests

r=requests.get('https://www.cbr-xml-daily.ru/daily_json.js')

str11=json.loads(r.text)
print(str11['Date'])
print(r.json()['Date'])

with open('cb.json','w') as f:
    json.dump(r.json(),f,indent=4)

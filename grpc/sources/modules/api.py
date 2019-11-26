import requests
import json

def GetData():
    url = 'http://faq-api:5000/db/1'
    res = requests.get(url)
    return res

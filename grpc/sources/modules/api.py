import requests
import json

def GetData():
    url = 'http://faq_api:5000/db/1'
    res = requests.get(url)
    return res

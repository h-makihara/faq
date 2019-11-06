import requests
import json

def GetData():
    url = 'http://API:5000/'
    res = requests.get(url)
    return res

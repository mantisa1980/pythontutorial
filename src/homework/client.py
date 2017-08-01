import json
import requests
import traceback
import time

def get_root():
    url = 'http://127.0.0.1:8000?param1=igs&param2=igsigs'
    try:
        response = requests.get(url,timeout=1)
        print "response={},content={}".format(response, response.content)
    except requests.exceptions.ReadTimeout:
        print traceback.format_exc()
    except Exception:
        print traceback.format_exc()

def post_root():
    payload ={
        "param1":"igs",
        "param2":"igsigs"
    }
    url = 'http://127.0.0.1:8000'
    headers = {'content-type': 'application/json' }
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers,timeout=1)
        print "post_root response={},content={}".format(response, response.content) 
    except requests.exceptions.ReadTimeout:
        print traceback.format_exc()
    except Exception:
        print traceback.format_exc()

get_root()
post_root()


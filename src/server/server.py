#!/usr/bin/env python         
# -*- coding: 
__author__ = "duyhsieh"

import falcon
import json
from account_manager import AccountManager


class RootHandler(object):
    def __init__(self):
        self.page = open("./index.html").read()

    def on_get(self, req, resp):
        resp.set_header('content-type', 'text/html')
        resp.body = self.page
        #resp.status = falcon.HTTP_200 # default

    def on_post(self, req, resp):
        resp.set_header('content-type', 'application/json')
        resp.body = json.dumps({'RootHandler': 'post'})
        resp.status = falcon.HTTP_200
        #resp.status = falcon.HTTP_500
        #resp.set_header('content-type', 'text/plain')
        #resp.body = 'Hello post'

class AccountHandler(object):
    def __init__(self, account_manager):
        self.account_manager = account_manager

    def on_get(self, req, resp):
        account = req.get_param("account")

        ret, result = self.account_manager.get_account(account)
        if ret:
            resp.body = json.dumps({"status":0, "result":result})
        else:
            resp.body = json.dumps({"status":-1, "result":result})

    def on_post(self, req, resp):
        data_stream = req.stream.read()
        dict_object = json.loads(data_stream)
        account = dict_object['account']
        nickname = dict_object['nickname']

        ret, result = self.account_manager.create_account(account, nickname)
        if ret:
            resp.body = json.dumps({"status":0,"result":result})
        else:
            resp.body = json.dumps({"status":-1,"result":result})

    def on_patch(self, req, resp):
        data_stream = req.stream.read()
        dict_object = json.loads(data_stream)
        account = dict_object['account']
        nickname = dict_object['nickname']

        ret, result = self.account_manager.patch_account(account, nickname)
        if ret:
            resp.body = json.dumps({"status":0, "result":result})
        else:
            resp.body = json.dumps({"status":-1, "result":result})
        
    def on_delete(self, req, resp):
        data_stream = req.stream.read()
        dict_object = json.loads(data_stream)
        account = dict_object['account']

        ret, result = self.account_manager.delete_account(account)
        if ret:
            resp.body = json.dumps({"status":0, "result":result})
        else:
            resp.body = json.dumps({"status":-1, "result":result})

api_router = falcon.API()
api_router.add_route('/', RootHandler())
api_router.add_route('/account', AccountHandler(AccountManager()))

# cmd: gunicorn -w 1 server:api_router --worker-class gevent

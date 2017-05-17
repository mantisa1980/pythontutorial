#!/usr/bin/env python         
# -*- coding: 


import gevent
from gevent import monkey;monkey.patch_all();
import falcon
import json

'''
build a RESTful API server
'''


class RootHandler(object):
    def on_post(self, req, resp):
        resp.body = json.dumps({"post":" root handler"})

    def on_get(self, req, resp):
        resp.body = json.dumps({"get":"root handler"})
        #resp.status = falcon.HTTP_200 # default

class HelloHandler(object):
    def on_post(self, req, resp):
        resp.body = json.dumps({"post":" hello"})

    def on_get(self, req, resp):
        resp.body = json.dumps({"get":"hello"})

api_router = falcon.API()
api_router.add_route('/', RootHandler())
api_router.add_route('/hello', HelloHandler())

# cmd: gunicorn -w 1 server:api_router --worker-class gevent

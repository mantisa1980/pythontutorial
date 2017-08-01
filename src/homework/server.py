#!/usr/bin/env python         
# -*- coding: utf-8 -*-
import falcon
import json
import time


class RootHandler(object):
    def on_get(self, req, resp):
        resp.set_header('content-type', 'text/plain')
        resp.body = "Hello Get"
        param1 = req.get_param('param1')
        param2 = req.get_param('param2')
        print "Get:param1={},param2={}".format(param1,param2)
        #time.sleep(5)

    def on_post(self, req, resp):
        try:
            resp.set_header('content-type', 'application/json')
            data_stream = req.stream.read()
            dict_object = json.loads(data_stream)
            dict_object['echo'] = 'OK'
            resp.body = json.dumps(dict_object)
            resp.status = falcon.HTTP_200
            print "Hello Post:dict={}".format(dict_object)
        except:
            print trackback.format_exc()
   
api_router = falcon.API()
api_router.add_route('/', RootHandler())

# cmd: gunicorn -w 1 server:api_router --worker-class gevent

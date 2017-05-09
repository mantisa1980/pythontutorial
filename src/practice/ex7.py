# -*- coding: utf-8 -*-
#import gevent
#from gevent import monkey;monkey.patch_all()
import os
import time

def app(environ, start_response):
    time.sleep(10)
    data = "Hello, World from pid:{}, ppid={}\n".format(os.getpid(), os.getppid())
    start_response("200 OK", [
       ("Content-Type", "text/plain"),
       ("Content-Length", str(len(data)))
    ])
    return iter([data])

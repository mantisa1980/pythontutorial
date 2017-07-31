# -*- coding: utf-8 -*-
import os
# cmd : gunicorn guni:app --bind 0.0.0.0 
# remove bind to accept connections from only localhost

def app(environ, start_response):
    data = "Hello, World from pid:{}, ppid={}\n".format(os.getpid(), os.getppid())
    start_response("200 OK", [
       ("Content-Type", "text/plain"),
       ("Content-Length", str(len(data)))
    ])
    return iter([data])

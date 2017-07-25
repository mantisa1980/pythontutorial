# -*- coding: utf-8 -*-
import os

def app(environ, start_response):
    data = "Hello, World from pid:{}, ppid={}\n".format(os.getpid(), os.getppid())
    start_response("200 OK", [
       ("Content-Type", "text/plain"),
       ("Content-Length", str(len(data)))
    ])
    return iter([data])

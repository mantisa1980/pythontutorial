# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server
import time


def my_app(environ, start_response):
    """a simple wsgi application"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    response_content = u" Hello 你好!<br>"
    for key,value in environ.iteritems():
        response_content = response_content + unicode( u"<b>{}</b>:{}<br>".format(str(key), str(value)) )
    
    # {{ to escape { character
    response_content = u"""
    <html>
    <head>
        <meta charset="UTF-8">
    </head>
    <style> b {{color: red }} </style>
    <body>
    {}
    </body>
    </html>
    """.format(response_content)

    #time.sleep(10)  # synchronous server demo
    return [response_content.encode('utf8')]

httpd = make_server('', 8000, my_app)
print "Serving on port 8000..."
httpd.serve_forever()

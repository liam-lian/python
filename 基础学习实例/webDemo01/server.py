
from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['<h1>Hello, %%s!</h1>']



httpd = make_server('', 10010, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()

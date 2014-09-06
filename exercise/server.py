# server
from wsgiref.simple_server import make_server
from hello import app

httpd = make_server('', 8991, app)
print 'Serving HTTP on port 8000...'
httpd.serve_forever()

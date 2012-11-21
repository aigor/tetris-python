import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import service

HandlerClass = service.TetrisService
ServerClass  = BaseHTTPServer.HTTPServer
Protocol     = "HTTP/1.0"

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8888
server_address = ('0.0.0.0', port)

HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, HandlerClass)

sa = httpd.socket.getsockname()
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()

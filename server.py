import os
from bottle import route, run, static_file
from bottle.ext.tornadosocket import TornadoWebSocketServer
import tornado.websocket


@route("/")
def hello_world():
	return static_file("index.html", root= 'static')

@route("/static/<name>")
def static(name):
	return static_file(name, root='static')

class EchoHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'Connected'

    def on_message(self, message):
        self.write_message(message)

    def on_close(self):
        print 'Connection closed'

 tornado_handlers = [
        (r"/websocket", EchoHandler)
    ]



#@get('/websocket', apply = [websocket])
#def handle_websocket(ws):
#    while True:
#        msg = ws.receive()
#        if msg is not None:
#            ws.send(msg)
#        else: break
run(host = '0.0.0.0', port=os.environ.get('PORT', 5000), reloader=True, server=TornadoWebSocketServer, handlers=tornado_handlers)
#run(host='0.0.0.0', port=os.environ.get('PORT', 5000), server=GeventWebSocketServer, debug= True)
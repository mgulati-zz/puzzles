import os
from bottle import route, run, static_file
from bottle.ext.websocket import GeventWebSocketServer
from bottle.ext.websocket import websocket

@route("/")
def hello_world():
        return static_file("index.html", root= 'static')

@route("/static/<name>")
def static(name):
		return static_file(name, root='static')


@route('/websocket', apply = [websocket])
def handle_websocket(ws):
    while True:
        try:
            message = ws.receive()
            wsock.send("Your message was: %r" % message)
        except WebSocketError:
            break

run(host='0.0.0.0', port=os.environ.get('PORT', 5000), server=GeventWebSocketServer, debug= True)
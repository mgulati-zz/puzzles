import os
from bottle import route, run, Bottle


app= Bottle()

@app.route("/")
def hello_world():
        return static_file(index.html, root= '/static')

@app.route("/static/<name>")
def static(name):
		return static_file(filename, root='/static')


@app.route('/websocket')
def handle_websocket():
    wsock = request.environ.get('wsgi.websocket')
    if not wsock:
        abort(400, 'Expected WebSocket request.')

    while True:
        try:
            message = wsock.receive()
            wsock.send("Your message was: %r" % message)
        except WebSocketError:
            break
from gevent.pywsgi import WSGIServer
from geventwebsocket import WebSocketHandler, WebSocketError

server = WSGIServer(("0.0.0.0", 8080), app,
                    handler_class=WebSocketHandler)
server.serve_forever()
import os
from bottle import route, run, static_file, Bottle, request, Response

import unicodedata
import gevent
from gevent.wsgi import WSGIServer
from socketio import socketio_manage
from socketio.namespace import BaseNamespace
from gevent import monkey
from socketio.server import SocketIOServer

monkey.patch_all()

app= Bottle()
app.debug= True



@app.route("/")
def hello_world():
	return static_file("index.html", root= 'static')

@app.route("/static/<name>")
def static(name):
	return static_file(name, root='static')


class MarkerMixin(object):
	def __init__(self, *args, **kwargs):
		super(MarkerMixin, self).__init__(*args, **kwargs)
		if 'room' not in self.session:
			self.session['room'] = ""  # a set of simple strings
		if 'unlocked' not in self.session:
			self.session['unlocked'] = False

	def join(self, room):
		"""Lets a user join a room on a specific Namespace."""
		if(self.session['room'] != room):
			self.session['room'] = room
			self.session['unlocked'] = False

	def unlock(self):
		self.session['unlocked'] = True
		room = self.session['room']
		pkt = dict(type = "event",
				   name = "unlocked")
		for sessid, socket in self.socket.server.sockets.iteritems():
			if 'room' not in socket.session:
				continue
			if room == socket.session['room'] and self.socket != socket:
				socket.send_packet(pkt)

class ChatNamespace(BaseNamespace, MarkerMixin):

	def on_join(self, room):
		self.room = room
		self.join(room)
		return True

	def recv_disconnect(self):
		self.disconnect(silent=True)
		return True

	def on_unlock(self):
		self.unlock()
		return True

@app.route('/ws/')
def socketio():
	try:
		socketio_manage(request.environ, {'/chat': ChatNamespace}, request)
	except:
		print("Exception while handling socketio connection")
	return Response()


SocketIOServer.serve
SocketIOServer(('0.0.0.0', os.environ.get('PORT', 5000)), app, heartbeat_interval=10, heartbeat_timeout=15, close_timeout=60, transports=['xhr-polling'], resource="socket.io").serve(app)



#@get('/websocket', apply = [websocket])
#def handle_websocket(ws):
#    while True:
#        msg = ws.receive()
#        if msg is not None:
#            ws.send(msg)
#        else: break
#run(host = '0.0.0.0', port=os.environ.get('PORT', 5000), reloader=True, server=TornadoWebSocketServer, handlers=tornado_handlers)
#run(host='0.0.0.0', port=os.environ.get('PORT', 5000), server=GeventWebSocketServer, debug= True)
import os
from bottle import route, run

@route("/")
def hello_world():
        return static_file(index.html, root= '/static')

@route("/static/<name>")
def static(name):
		return static_file(filename, root='/static')

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
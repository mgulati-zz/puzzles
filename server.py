from bottle import route, run

@route('/hello')
def routehello():
    return "hello"

run(host='localhost', port=8080, debug=True)
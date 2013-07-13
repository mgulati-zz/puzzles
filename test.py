from bottle import route, run, request, static_file
import utils
import json
import math

@route("/")
def hello_world():
	return static_file("index.html", root= 'static')

@route("/static/<name>")
def static(name):
	return static_file(name, root='static')

@route("/getGoodies")
def getGoodies():
	data = {
		'goodies': {
			'first' : {
				'description': 'this is the first marker',
				'members': ['Aya', 'Jordan', 'Devon'],
				'location': {
					'latitude' : 37.524975368048196,
					'longitude' : -122.310791015625
				}
			},
			'second': {
				'description': 'this is the second marker',
				'members': ['ben', 'bob', 'billy'],
				'location': {
					'latitude' : 37.58594229860422,
					'longitude' : -122.49343872070312
				}
			},
			'third': {
				'description': 'this is the third marker',
				'members': ['Jay', 'Jared', 'Mayank'],
				'location': {	
					'latitude' : 37.72130604487683,
					'longitude' : -122.45361328125
				}
			}
		}
	}

	latitude = request.query.latitude
	longitude = request.query.longitude

	for goodie in data['goodies']:
		if (math.fabs(data['goodies'][goodie]['location']['latitude'] - float(latitude)) < 0.03 and
			math.fabs(data['goodies'][goodie]['location']['longitude'] - float(longitude)) < 0.03):
				data['enabledGoodie'] = goodie

	return json.dumps(data);

run(host="0.0.0.0", port = 8080, debug = True )

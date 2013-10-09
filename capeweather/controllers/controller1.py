#!./venv/bin/python

# from flask import request #, make_response

from flask import request, render_template, make_response

from time import time
import httplib  
import urllib
import json

from capeweather import app
from . import valueFromRequest

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'You want path: %s' % path

@app.route('/')
def index():
	''' This shows how to render a template. '''
		
	templateDict = {}#{"header":"Is it cape weather?"}
	return render_template("index.html", **templateDict)

@app.route('/getWeather', methods=['GET', 'POST'])
def getWeather():
	'''
	If accepting both GET and POST methods, use the local
	"valueFromRequest" method (defined in controllers.__init__.py).
	This handles both methods, and you can specify whether each
	parameter value should be made lower case, returned as a Boolean
	(e.g. for flags with no value), or parsed into a list from a
	comma-separated string.
	'''
	lat = float(valueFromRequest(key="lat", request=request))
	long = float(valueFromRequest(key="long", request=request))

	results=getWeatherFromAPI(lat,long)
		
	response=make_response(json.dumps(results))
	response.headers["Access-Control-Allow-Origin"]="http://isitcapeweather.com"
	return response
	
#-------------------------------- Non page control functions here ------------------------
def getWeatherFromAPI(lat,long):
	currentTime=time()
	key="{0:.1f}_{1:.1f}".format(lat,long)


	# if the location has been queried before, check when it was last queried
	#if key in getWeatherFromAPI.lastCalls.keys():
	#	lastTime=getWeatherFromAPI.lastCalls[key]["time"] # we just keep the last time the API was called
	#	
	#	# only make an API call for a location once per hour
	#	if currentTime-lastTime<60*60: 
	#		return {"temp":getWeatherFromAPI.lastCalls[key]["temp"],"rain":getWeatherFromAPI.lastCalls[key]["rain"]}
	

	# we get here if neither the time nor place is recently checked.
	
	# call the API
	APIKey="this is not an api key - get your own from api.worldweatheronline.com"
	params='q={0:.3f},{1:.3f}&format=json&key={2}'\
		.format(lat,long,APIKey)

	conn = httplib.HTTPConnection("api.worldweatheronline.com")
	conn.request("GET", "/free/v1/weather.ashx?"+params)
	r1 = conn.getresponse()

	if r1.status == httplib.OK:
		output=r1.read()	
		weatherObj=json.loads(output)

		temp=weatherObj['data']['current_condition'][0]['temp_F']
		rain=False
		weatherCode=float(weatherObj['data']['current_condition'][0]['weatherCode'])
		
		if weatherCode>143 and weatherCode!=248:
			rain=True 
		getWeatherFromAPI.lastCalls[key]={"temp":temp,"rain":rain}
		conn.close()
		return {"temp":temp,"rain":rain,"time":currentTime,"code":weatherCode}
	else:
		conn.close()
		return {"error":r1}

getWeatherFromAPI.lastCalls={}	










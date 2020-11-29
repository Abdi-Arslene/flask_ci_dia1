from flask import Flask
from redis import Redis, RedisError
import socket

redis = Redis(host="redis-server", db=0)

app = Flask(__name__)

@app.route('/')

def hello():
	return "<h1> wesh alors </h1>"

@app.route('/visit')
def incr_counter():
	try:
		visits = redis.incr("counter")
	except:
		visits = "<i> jai pas pu me connecter a redis server </i>"
	html= "<h1>Nombre de visites : {}</h1>".format(visits)
	return html
if __name__ == "__main__":
	app.run(debug=True, port=80, host="0.0.0.0")
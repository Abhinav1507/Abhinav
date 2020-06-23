from flask import Flask, render_template, request, make_response, g 
from redis import Redis
import os 
import socket 
import random 
import json
option_a = os.getenv('OPTION_A', "Cats") 
option_b = os.getenv('OPTION_B', "Dogs") 
hostname = socket.gethostname()
app = Flask( name ) 
def get_redis():
if not hasattr(g, 'redis'):
g.redis = Redis(host="redis", db=0, socket_timeout=5) 
return g.redis
@app.route("/", methods=['POST','GET']) 
def hello():
voter_id = request.cookies.get('voter_id') 
if not voter_id:
voter_id = hex(random.getrandbits(64))[2:-1]
vote = None
if request.method == 'POST':
redis = get_redis()
vote = request.form['vote']
data = json.dumps({'voter_id': voter_id, 'vote': vote}) 
redis.rpush('votes', data)
resp = make_response(render_template( 
'index.html',
option_a=option_a, 
option_b=option_b, 
hostname=hostname, 
vote=vote,
))
resp.set_cookie('voter_id', voter_id) 
return resp
if __name == " main ":
app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
Main Docker-compose 
version: "3"
services: 
vote:
build: ./vote
command: python app.py 
volumes:
- ./vote:/app 
ports:
- "5000:80"
networks:
- front-tier
- back-tier
result:
build: ./result
command: nodemon server.js 
volumes:
- ./result:/app 
ports:
- "5001:80"
- "5858:5858"
networks:
- front-tier
- back-tier
worker: 
build:
context: ./worker 
depends_on:
- "redis" 
networks:
- back-tier
redis:
image: redis:alpine 
container_name: redis 
ports: ["6379"]
networks:
- back-tier
db:
image: postgres:9.4 
container_name: db 
volumes:
- "db-data:/var/lib/postgresql/data" 
networks:
- back-tier
volumes: 
db-data:
networks: 
front-tier: 
back-tier:

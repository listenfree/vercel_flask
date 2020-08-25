from flask import make_response,Response,request,redirect,Flask
from requests import get
from flask_sockets import Sockets
import gevent
app = Flask(__name__)
sockets = Sockets(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    image_binary = get("https://loremflickr.com/600/400").content
    response = make_response(image_binary)
    response.headers.set('Content-Type', 'image/jpeg')
    return response
    #return Response("<h1>Flask</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")

@sockets.route('/eeee')
def eeee_socket(ws):
    while not ws.closed:
        message = ws.receive()
        ws.send(message)

from flask import Flask, Response
from requests import get
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    image_binary = get("https://loremflickr.com/600/400").content
    response = make_response(image_binary)
    response.headers.set('Content-Type', 'image/jpeg')
    return response
    #return Response("<h1>Flask</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")


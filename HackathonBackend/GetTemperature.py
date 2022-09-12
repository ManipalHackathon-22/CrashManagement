import json
from sre_compile import isstring
from flask import Flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
import SerialReader
import DbConn

app = Flask(__name__)
cors = CORS(app)
cors = CORS(app, resources={
    r"/*": {
        "origins" : "*"
    }
})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/temp', methods=['GET'])
def Temperature_alert():
    temperature = SerialReader.Temperature_check()

    if temperature > 26.5:
        return 'HIGH!'
    else:
        return 'LOW'

@app.route('/', methods = ['GET'])
def hello():
    return("hello")


@app.route('/crashInfo', methods=['POST'])
def Post_crash_info():
    content = request.json
    print(content['name'])
    
    name = content['name']
    ph = content['ph']
    location = content['location']
    crashconfirm = content['crashconfirm']

    DbConn.PutUserInfo(name, ph, location, crashconfirm)
    return jsonify(content)

@app.route('/crashInfo', methods = ['GET'])
def get_crash_info():
    userInfo = DbConn.GetUserInfo()
    return jsonify(userInfo)


if __name__ == "__main__":
    app.run(debug=False, port = "5000")

    
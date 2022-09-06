from crypt import methods
import json
from flask import Flask
from flask import request, jsonify
#import SerialReader
import DbConn

app = Flask(__name__)


# @app.route('/', methods=['GET'])
# def Temperature_alert():
#     temperature = SerialReader.Temperature_check()
#     if temperature > 26.5:
#         return jsonify({'message' : 'HIGH!'})
#     else:
#         return jsonify({'message' : 'LOW'})



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
    app.run(debug=False)

    
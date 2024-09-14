from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/get', methods=['GET'])
def get_example():
    response = {
        'message': 'GET request response',
        'headers': dict(request.headers)
    }
    return jsonify(response)


@app.route('/post', methods=['POST'])
def post_example():
    data = request.json
    response = {
        'message': 'POST request',
        'received_data': data
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
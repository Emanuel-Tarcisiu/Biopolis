from flask import Flask, request, jsonify, send_file
import os
from flask_cors import CORS
from veg_health import get_new_vegHealth_png


app = Flask(__name__)
CORS(app)


@app.route('/city_total_area', methods=['GET'])
def get_city_total_area():
    # data = request.json
    # a = data.get('a')
    # b = data.get('b')
    
    response = {
        "rasp": "Hello world!"
    }
    return jsonify(response)


@app.route('/vegetation_health', methods=['GET'])
def get_vegetation_health():
    image_path = 'output/ndvi.png'

    get_new_vegHealth_png()

    print("s-a calc noua img")

    if os.path.exists(image_path):
        return send_file(image_path, mimetype='image/png')
    else:
        return jsonify({"error": "Image not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
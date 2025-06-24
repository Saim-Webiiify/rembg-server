from flask import Flask, request, send_file
from flask_cors import CORS
from rembg import remove
from io import BytesIO
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "rembg-server is running!"

@app.route("/api/remove", methods=["POST"])
def remove_bg():
    if "file" not in request.files:
        return {"error": "No file part"}, 400

    file = request.files["file"]
    if file.filename == "":
        return {"error": "No selected file"}, 400

    input_data = file.read()
    output_data = remove(input_data)
    return send_file(BytesIO(output_data), mimetype="image/png")

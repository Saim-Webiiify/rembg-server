from flask import Flask, request, send_file
from flask_cors import CORS
from rembg import remove
from io import BytesIO
import os

app = Flask(__name__)
CORS(app)  # ✅ enable CORS for all routes

@app.route("/api/remove", methods=["POST"])
def remove_bg():
    img = request.files.get("file")
    if not img:
        return {"error": "Missing file"}, 400
    result = remove(img.read())
    return send_file(BytesIO(result), mimetype="image/png")

@app.route("/", methods=["GET"])
def welcome():
    return "rembg-server is running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

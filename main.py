from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return jsonify({"message": "Hola Mundo en REST API en python"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

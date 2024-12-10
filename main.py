from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)  # Initialise Swagger

@app.route("/", methods=["GET"])
def hello_world():
    """
    Welcome message
    ---
    responses:
      200:
        description: Returns a "Hello World" message
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: Hello World from REST API in python
    """
    return jsonify({"message": "Hello World from REST API in python"})

if __name__ == "__main__":
    port = 5000
    print(f"Swagger documentation at: \033[92mhttp://localhost:{port}/apidocs\033[0m")
    app.run(host="0.0.0.0", port=port, debug=True)

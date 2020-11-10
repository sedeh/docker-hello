from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    output = {'message': 'Hello from Docker!'}
    response = jsonify(output)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

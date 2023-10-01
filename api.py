from flask import Flask
from flask import request

from autos_dat import get_price, set_price

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/api/<marca>", methods=["GET"])
def get_ticker(marca):
    return get_price(marca)


@app.route("/api/<marca>", methods=["POST"])
def post_ticker(marca):
    document = get_price(marca)
    return set_price(document)


@app.route("/api/multiple/", methods=["GET"])
def api_multiple_get():
    marcas = request.args.get('marcas')
    marcas = marcas.split(',')

    result = []
    for t in marcas:
        result.append(get_price(t))
    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)

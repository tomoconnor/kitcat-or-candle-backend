from flask import Flask, jsonify, render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
import random

kitkats = []
candles = []

app.logger.info('Loading Kitkats')
with open("data/kit-kats-unique") as k:
    kitkats = [line.rstrip() for line in k]
app.logger.info("Loading Yankee Candles")
with open("data/yankee-candles") as y:
    candles = [line.rstrip() for line in y]


@app.route('/api/new')
def new():
    ks = [('k', k) for k in random.choices(kitkats, k=10)]
    cs = [('c', c) for c in random.choices(candles, k=10)]
    gamedata = ks+cs
    random.shuffle(gamedata)
    return jsonify(data=gamedata)
    # return jsonify(c=random.choices(candles, k=10), k=random.choices(kitkats,k=10))

@app.route("/api/kitkats")
def getKitkats():
    return jsonify(kitkats=kitkats)

@app.route("/api/candles")
def getCandles():
    return jsonify(candles=candles)

if __name__ == "__main__":
    app.run()
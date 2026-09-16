from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "application": "Jenkins Demo API",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return jsonify({
        "a": a,
        "b": b,
        "result": a + b
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

existing_models = ["Beedle", "Crossroads", "M2", "Panique"]

from flask import Flask, abort

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "Welcome to Flatiron Cars"


@app.route("/<model>", methods=["GET"])
def get_model(model):
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"No models called {model} exists in our catalog"


if __name__ == "__main__":
    app.run(port=5555, debug=True)

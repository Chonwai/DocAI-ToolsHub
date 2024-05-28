from flask import Flask
from v1.api import api_bp

app = Flask(__name__)

app.register_blueprint(api_bp, url_prefix="/api/v1")


@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"

from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Indrajeet DevOps Kubernetes Project!"

@app.route("/health")
def health():
    return "OK"

@app.route("/version")
def version():
    return os.getenv("APP_VERSION", "v1")

app.run(host="0.0.0.0", port=5000)


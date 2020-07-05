print("Needs implementation")

from flask import Flask, jsonify, request, render_template

app = Flask(__name__, static_folder="client/build")

@app.route('/')
def index():
    return app.send_static_file("index.html")

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

print("Running on  http://localhost:8080/")
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, threaded=False)
